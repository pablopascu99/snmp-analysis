from confluent_kafka import Consumer
from cassandra.cluster import Cluster
import json
import sys

c = Consumer({'bootstrap.servers':'localhost:9091','group.id':'counting-group','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

#print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['user-tracker'])

cluster = Cluster(contact_points=['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS snmp_traps
    WITH REPLICATION =
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
    """)
session.execute("""
    USE snmp_traps;
    """)
session.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (user_id int, user_name text, user_address text, platform text, PRIMARY KEY (user_id));
    """)
session.set_keyspace('snmp_traps')

def main():

    while True:
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=json.loads(msg.value().decode('utf-8'))
        
        session.execute(
            """
            INSERT INTO usuarios (user_id, user_name, user_address, platform)
            VALUES (%s, %s, %s, %s)
            """,
            (data['user_id'],
             data['user_name'],
             data['user_address'],
             data['platform']))
    c.close()

main()
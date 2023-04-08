from confluent_kafka import Consumer
import json
import psycopg2

c = Consumer({'bootstrap.servers':'kafka1:19091','group.id':'counting-group','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

#print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['user-tracker'])

#establishing the connection
conn = psycopg2.connect(database="postgres", user='postgres', password='postgres', host='postgres', port= '5432')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

sql= '''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR (255),
    user_address VARCHAR (255),
    platform VARCHAR (255)
)'''

cursor.execute(sql)
conn.commit()
def main():

    while True:
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        #Setting auto commit false
        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        data=json.loads(msg.value().decode('utf-8'))
        cursor.execute(""" INSERT INTO users (user_id, user_name, user_address, platform) VALUES (%s,%s,%s,%s)""",
            (data['user_id'],
             data['user_name'],
             data['user_address'],
             data['platform']))

main()
from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging
import random 
fake=Faker()

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

p = Producer({'bootstrap.servers':'localhost:9091'})

print('Kafka Producer has been initiated...')

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

def main():
    for i in range(1000000):
        data={
            'user_id': fake.random_int(min=20000, max=100000),
            'user_name':fake.name(),
            'user_address':fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
            'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
            }
        m=json.dumps(data)
        p.poll(1)
        # Producimos en el topic user-tracker
        p.produce('user-tracker', m.encode('utf-8'),callback=receipt)
        p.flush()
        time.sleep(1)

main()
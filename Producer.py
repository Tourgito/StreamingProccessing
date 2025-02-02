from confluent_kafka import Producer
from random import choice
from time import sleep

Phones = ['Samsung galaxy 9', 'Apple iphone 11', 'Huwai P30']  #Phones

p = Producer({'bootstrap.servers': 'localhost:9092'}) #Producer parameters

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

while True:
    Phone = choice(Phones)
    sleep(1)
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('Test', value=Phone.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()

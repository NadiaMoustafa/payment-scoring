import json
import time
import numpy as np # type: ignore
from kafka import KafkaProducer # type: ignore

# Producer config
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # the same port in Docker Compose
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print(" Kafka Producer started...")

transaction_id = 0
while True:
    transaction = {
        "transaction_id": transaction_id,
        "amount": float(np.random.uniform(10, 1000)),
        "customer_age": int(np.random.randint(18, 70)),
        "transaction_type": int(np.random.randint(0, 2))
    }
    
    producer.send('transactions', transaction)
    print(f" Sent transaction {transaction_id}")
    
    transaction_id += 1
    time.sleep(1)  

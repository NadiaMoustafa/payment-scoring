import json
import pickle
import mysql.connector # type: ignore
from kafka import KafkaConsumer # type: ignore

#  load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
print(" Model loaded!")

# MySQL
db = mysql.connector.connect(
    host="localhost",
    user="nadia",
    password="nadia123",
    database="payments"
)
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS scored_transactions (
    transaction_id INT PRIMARY KEY,
    amount FLOAT,
    customer_age INT,
    transaction_type INT,
    score FLOAT
)
""")
db.commit()
print(" MySQL ready!")

#  Consumer
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
print(" Kafka Consumer started...")

for message in consumer:
    transaction = message.value
    X = [[
        transaction["amount"],
        transaction["customer_age"],
        transaction["transaction_type"]
    ]]
    score = model.predict_proba(X)[0][1]  # Fraud
    transaction_id = transaction["transaction_id"]

    cursor.execute("""
    INSERT INTO scored_transactions (transaction_id, amount, customer_age, transaction_type, score)
    VALUES (%s, %s, %s, %s, %s)
    """, (transaction_id, transaction["amount"], transaction["customer_age"], transaction["transaction_type"], score))
    
    db.commit()
    print(f" Transaction {transaction_id} scored: {score:.2f}")

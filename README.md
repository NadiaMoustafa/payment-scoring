# Real-Time Payment Scoring Model

This project implements an End-to-End real-time payment scoring system using:
- Apache Kafka for streaming transactions
- A pre-trained machine learning model (Logistic Regression) for fraud detection / credit scoring
- MySQL for storing the scoring results

The system reads payment transactions from Kafka in real-time, applies the model to score each transaction, and stores the results in MySQL.

## Key Components

1. **Data Ingestion (Kafka):** Consumes real-time payment transactions from a Kafka topic.
2. **Transaction Scoring (Machine Learning Model):** Applies a pre-trained model to score each transaction.
3. **Data Storage (MySQL):** Stores the scored transactions for reporting and analysis.

## Requirements

- Docker Desktop (with WSL2 for Linux containers)
- Python 3.9+
- Python libraries (see `requirements.txt`)

## Running the Project

**1. Clone the Repository** : git clone https://github.com/NadiaMoustafa/payment-scoring.git

**2. Run Docker Services** : docker-compose up -d **(but Make sure Docker Desktop is installed and running)**

**3. Check that the containers are running**: docker ps

**4. Create a virtual environment**: python -m venv venv

**5. Activate the environment** : venv\Scripts\activate **(Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass write this before if you faced any issue)**

**6. Install the project dependencies**: pip install -r requirements.txt

**7. Model** : The trained model is already saved as **model.pkl**, so you don’t need to retrain it. You can use it directly. (just to save your time)

**8.  Run the Project** :
  **Start the Producer – sends real-time transactions to Kafka**: python producer.py
  **Start the Consumer – reads transactions from Kafka, scores them using the pre-trained model, and stores the results in MySQL** : python consumer.py
  
**9. Check Results in MySQL** : Open any MySQL client (e.g., DBeaver) with the credentials provided in the project. The scored transactions will be available in the **table: scored_transactions**

## Overview about the Training (The model)

1. Used 500 synthetic transactions (used number like 500 to make the process faster as it is a prototype but i made it Scalable for the future)
2. Split into 80% training / 20% testing
3. Model trained with max_iter=200 and solver='liblinear' (optimized for small datasets)
4. Saved Model: The trained model is stored in model.pkl for real-time scoring in the consumer pipeline

## Implementation Phases

1. Setup & Configuration : (docker-compose to work Kafka + Zookeeper + MySQL)
2. Model Integration : The model is trained and saved as a pkl file so the consumer can use it directly
3. Real-Time Processing: Consumer : it runs in real-time read the transactions from kafka(producer) & use the model to score the paymets then write into mySQL
4. Testing & Validation : finally you can test by open the DB in your device and see the scores (the results) in the real-time
   
## THE DB TABLE 

<img width="997" height="402" alt="Screenshot 2025-11-23 140259" src="https://github.com/user-attachments/assets/b1674055-4e7b-481e-96a6-1d9ff7dd7a9d" />



















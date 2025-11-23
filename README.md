# Real-Time Payment Scoring System


This project implements a real-time payment scoring system using:

- Apache Kafka for streaming transactions
- A pre-trained machine learning model for fraud detection / credit scoring
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

1. **Start the infrastructure** (Kafka + MySQL) using Docker Compose:
   ```bash
   docker-compose up -d


python train_model.py
python producer.py
python consumer.py
docker exec -it mysql mysql -unadia -pnadia123 payments


open it again 
first clone it by 
> git clone https://github.com/NadiaMoustafa/payment-scoring.git
> make sure you downloaded the docker disctop and runned this : docker-compose up -d
> then check if docker running : docker ps
> make an environment : python -m venv venv
> then activated : Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> venv\Scripts\activate
> then install the requirments : pip install -r requirements.txt 
> supposed to run traned.model but i aleadry runned it and save the model in pkl file so i can use it (saving your time)
> run the producer to make kafka send the real time transactions : python producer.py
> and run in another terminal the consumer to make the model calculate the score and save the result in the mqsql database :python .\consumer.py
> then open any MYSQl driver to open the database with its credintail apove and you will see the transactions with model score saved in table called : scored_transactions

> 
## 6️⃣ ملاحظات
```markdown
- All transactions are synthetic for demonstration purposes.
- The model is pre-trained and saved as `model.joblib`.
- Docker ensures that Kafka and MySQL run with correct configuration.


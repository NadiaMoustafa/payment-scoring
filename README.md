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



## 6️⃣ ملاحظات
```markdown
- All transactions are synthetic for demonstration purposes.
- The model is pre-trained and saved as `model.joblib`.
- Docker ensures that Kafka and MySQL run with correct configuration.

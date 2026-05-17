# OpenWeather Kafka Streaming Pipeline

A real-time weather data streaming pipeline built using the OpenWeather API, Apache Kafka, Docker, and Python.

This project demonstrates how to stream weather data from an external API into Kafka using a producer-consumer architecture.

---

## 📌 Project Overview

The pipeline performs the following steps:

1. Extracts live weather data from the OpenWeather API
2. Sends weather data to a Kafka topic using a Kafka Producer
3. Consumes streamed weather data using a Kafka Consumer
4. Processes and displays the streamed records in real time

---

## 🏗️ Architecture

```text
OpenWeather API
       ↓
Kafka Producer (producer.py)
       ↓
Kafka Topic
       ↓
Kafka Consumer (consumer.py)
       ↓
Processed Streaming Data
```

---

## ⚙️ Technologies Used

- Python
- Apache Kafka
- Docker
- Docker Compose
- OpenWeather API
- kafka-python
- Jupyter Notebook

---

## 📂 Project Structure

```text
openweather-kafka_confluent-project/
│
├── producer.py
├── consumer.py
├── test.ipynb
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 📄 Project Files

### 📌 Producer

Streams weather data into Kafka topics.

- [producer.py](https://github.com/Damaa-C/openweather-kafka_confluent-project/blob/main/producer.py)

### 📌 Consumer

Consumes and processes weather data from Kafka topics.

- [consumer.py](https://github.com/Damaa-C/openweather-kafka_confluent-project/blob/main/consumer.py)

### 📌 Jupyter Notebook

Used for testing and experimentation.

- [test.ipynb](https://github.com/Damaa-C/openweather-kafka_confluent-project/blob/main/test.ipynb)

### 📌 Dependencies

Project dependencies and Python packages.

- [requirements.txt](https://github.com/Damaa-C/openweather-kafka_confluent-project/blob/main/requirements.txt)

---

## 🚀 Setting Up the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Damaa-C/openweather-kafka_confluent-project.git

cd openweather-kafka_confluent-project
```

---

## 🐳 Running Kafka with Docker

### Start Kafka and Zookeeper

```bash
docker compose up -d
```

### Verify Running Containers

```bash
docker ps
```

Expected containers:

- kafka
- zookeeper

---

## 📸 Docker Kafka Containers Running

![Docker Kafka Containers](https://github.com/Damaa-C/openweather-kafka_confluent-project/blob/main/Screenshot%20(22).png)

---

## 📦 Create Virtual Environment

```bash
python3 -m venv kafka_env

source kafka_env/bin/activate
```

---

## 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variables

Create a `.env` file:

```bash
nano .env
```

Add your OpenWeather API key:

```env
OPENWEATHER_API_KEY=your_api_key
```

Get a free API key from:

https://home.openweathermap.org/api_keys

---

## ▶️ Running the Pipeline

### Step 1: Start Kafka Consumer

```bash
python3 consumer.py
```

### Step 2: Start Kafka Producer

Open another terminal:

```bash
python3 producer.py
```

---

## 📸 Kafka Producer Running

![Kafka Producer](https://github.com/Damaa-C/openweather-kafka_confluent-project/blob/main/Screenshot%20(20).png)

---

## 📸 Kafka Consumer Streaming Data

![Kafka Consumer](https://github.com/Damaa-C/openweather-kafka_confluent-project/blob/main/Screenshot%20(21).png)

---

## 📡 Kafka Streaming Flow

```text
Producer → Kafka Broker → Kafka Topic → Consumer
```

---

## 📊 Example Output

```text
Weather Data Sent:
{
  "city": "Nairobi",
  "temperature": 22,
  "humidity": 68
}
```

Consumer Output:

```text
Received Weather Data:
{
  "city": "Nairobi",
  "temperature": 22,
  "humidity": 68
}
```

---

## 📸 Real-Time Weather Data Streaming

![Weather Streaming](https://github.com/Damaa-C/openweather-kafka_confluent-project/blob/main/Screenshot%20(24).png)

---

## 🧪 Testing

The notebook below was used for API testing and experimentation:

- [test.ipynb](https://github.com/Damaa-C/openweather-kafka_confluent-project/blob/main/test.ipynb)

---

## 🐳 Docker Services

This project uses:

| Service | Purpose |
|---|---|
| Kafka | Message broker |
| Zookeeper | Kafka coordination service |

---

## 📚 Concepts Demonstrated

- Real-time data streaming
- Kafka producer-consumer architecture
- Dockerized Kafka setup
- API integration
- Event-driven pipelines
- Python streaming applications

---

## 🔮 Future Improvements

- Load streamed data into PostgreSQL
- Add Airflow orchestration
- Add Kafka topic monitoring
- Implement schema validation
- Dockerize producer and consumer services
- Deploy pipeline to cloud infrastructure

---

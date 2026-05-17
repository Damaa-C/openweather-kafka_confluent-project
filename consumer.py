from kafka import KafkaConsumer
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import json
import pandas as pd

load_dotenv()

Postgres_URI = os.getenv("POSTGRES_URI")

engine = create_engine(Postgres_URI)

consumer = KafkaConsumer(
    'weather_raw',
    bootstrap_servers = 'localhost:9092',
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    value_deserializer = lambda x : json.loads(x.decode('utf-8'))
)

print("Consumer started listening ...")

for message in consumer :

    try :
        
        data = message.value
        
        transformed_data = {
            "city" : data.get("name"),
            "temperature" : data.get("main",{}).get("temp"),
            "humidity" : data.get("main",{}).get("humidity"),
            "pressure" : data.get("main",{}).get("pressure"),
            "weather" : data.get("weather",[{}])[0].get("main"),
            "description" : data.get("weather",[{}])[0].get("description"),
            "wind_speed" : data.get("wind",{}).get("speed")
        }

        df = pd.DataFrame([transformed_data])

        print("\n Transfromed weather data")

        df.to_sql("weather_kafka", con=engine, if_exists="append",index=False)

        print(f"Loaded weather data for {transformed_data['city']}")
        
    except Exception as e :

        print(f"Consumer error : {e}")
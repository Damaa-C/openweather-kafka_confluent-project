from kafka import KafkaProducer
import time
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY  = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")
LANG     = os.getenv("LANG")

topic = "weather_raw"

producer = KafkaProducer(
    bootstrap_servers = 'localhost:9092',
    value_serializer = lambda v : json.dumps(v).encode('utf-8')
)

Cities = ['Nairobi','Accra','Cape Town','Riga','Brussels','Moscow','Seoul','London','Sucre']

while True :

    for city in Cities :

        url = f"https://{API_HOST}/city?city={city}&lang={LANG}"

        headers = {'x-rapidapi-host': API_HOST,
                   'x-rapidapi-key' : API_KEY
                   }
        
        try :

            response = requests.get(url,headers=headers)

            if response.status_code == 200 :
                weather_data = response.json()

                producer.send(topic,value = weather_data)

                print(f"Sent weather data for {city}")
        
            else :
                print(f"Failed for {city} : {response.status_code} ")
        
        except Exception as e :

            print(f"Error for {city} : {e}")
    
    producer.flush()

    time.sleep(1)

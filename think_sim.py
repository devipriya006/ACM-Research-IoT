import requests  
import random    
import time  


API_KEY = "9Q44A4XCONLMELO4"  
URL = "https://api.thingspeak.com/update"

while True:
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(30, 70), 2)
    
    
    response = requests.get(URL, params={
        "api_key": API_KEY,
        "field1": temperature,
        "field2": humidity
    })


    print(f"Sent data -> Temperature: {temperature}°C, Humidity: {humidity}%")

    time.sleep(15)

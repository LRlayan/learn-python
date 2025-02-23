import requests as rq

base_url = 'https://api.open-meteo.com/v1/forecast'

def fetch_weather(latitude,longitude,current_info):
    params = {
        'latitude':latitude,
        'longitude':longitude,
        'current':current_info
    }
    
    response = rq.get(base_url,params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return 'faild retrival data. please try again!'    


def parse_weather_data(response):
    print("temperature_2m : ",response['current']['temperature_2m'])
    print("wind_speed_10m : ",response['current']['wind_speed_10m'])
    
weather_details = fetch_weather(51.5074,-0.1278,'temperature_2m,wind_speed_10m')
parse_weather_data(weather_details)
print(weather_details)
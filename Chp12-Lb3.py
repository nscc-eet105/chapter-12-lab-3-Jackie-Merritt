#Jackie-Merritt_Chp12-Lb3_7/13/2025
import requests

def main():
    # https://api.openweathermap.org/data/2.5/weather?zip=43567,us&appid=002ec48f71985084985b01726b4f892d&units=imperial
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=43567,us&appid=002ec48f71985084985b01726b4f892d&units=imperial")

    if response:
        response_dict = response.json()
        #print(response_dict["main"]["temp"])
        #print(f'Current Weather for {response_dict["name"]}')
        print(response_dict["weather"]["main"])
        #print(f'Temperature: {response_dict["main"]["temp"]} Degrees\nFeels Like: {response_dict["main"]["feels_like"]} Degrees')
        #print(f'Humidity: {response_dict["main"]["humidity"]}%\nWind: {response_dict["wind"]["speed"]} Knots @ {response_dict["wind"]["deg"]} Degrees')
    



if __name__ == '__main__':
    main()

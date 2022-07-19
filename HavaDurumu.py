
import requests

url = "http://api.airvisual.com/v2/countries?key=290697f5-f7bf-48b5-ade3-f3af5e830eaa"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)


def get_countries():
    url = "http://api.airvisual.com/v2/countries?key=290697f5-f7bf-48b5-ade3-f3af5e830eaa"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    for json in response.json()["data"]:
        print(json['country'])


def get_cities(country):

    url = f"http://api.airvisual.com/v2/states?country={country}&key=290697f5-f7bf-48b5-ade3-f3af5e830eaa"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    for json in response.json()["data"]:
        print(json["state"])


def get_detailed_city(country, city):

    url = f"http://api.airvisual.com/v2/city?city={city}&state={city}&country={country}&key=290697f5-f7bf-48b5-ade3-f3af5e830eaa"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    json = response.json()["data"]["current"]["weather"]
    tempreture = json["tp"]
    humidity = json["hu"]
    wind_speed = json["ws"]
    print(f"Tempreture: {tempreture}")
    print(f"Humidity: {humidity}")
    print(f"Wind Speed: {wind_speed}")

    # print(json['pollution'])
    # print(json['weather'])

    """
{
        "ts": "2017-02-01T03:00:00.000Z",  //timestamp
        "aqius": 21, //AQI value based on US EPA standard
        "aqicn": 7, //AQI value based on China MEP standard
        "tp": 8, //temperature in Celsius
        "tp_min": 6, //minimum temperature in Celsius
        "pr": 976,  //atmospheric pressure in hPa
        "hu": 100, //humidity %
        "ws": 3, //wind speed (m/s)
        "wd": 313, //wind direction, as an angle of 360° (N=0, E=90, S=180, W=270)
        "ic": "10n" //weather icon code, see below for icon index
      }, 
      """


print("ulke seciniz: ")
get_countries()
ulke = input("ülke seciniz :")

get_cities(ulke)

sehir = input("sehir seciniz :")
get_detailed_city(ulke, sehir)

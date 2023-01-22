import requests
API_KEY = "3063858c7ccd2898a3693026d30c5f4e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city = input("INTRODU NUMELE ORASULUI: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
rasp = requests.get(request_url)
if rasp.status_code == 200:
    data = rasp.json()
    vremea = data['weather'][0]['description']
    temp = round(data["main"]["temp"] -273.15, 2)
    vantspeed = data['wind']['speed']
    vantdeg = data['wind']['deg']

    print("VREMEA: ", vremea)
    print("TEMPERATURA: ", temp, " C")
    print("VANT: ", "Speed: ", vantspeed)
    print("VANT: ", "Deg: ", vantdeg)


else:
    print("AVEM O EROARE: |")




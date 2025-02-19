import requests
city = input()
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city +
                    "&appid=8c5483ca81e4064fd0c7bb62bca9b8b3").json()

print(data)

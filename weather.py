import requests

API_KEY = "559159a046bcae5b3042e360bf070db6"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print(data)

if response.status_code == 200:

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print("\nWeather Report")
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")

else:
    print("Error:", data["message"])
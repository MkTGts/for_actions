import requests

response = requests.get(
    url="https://ya.ru"
)

print(response.status_code)
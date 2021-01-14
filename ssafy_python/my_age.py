import requests

name = 'christoper'
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()
age2 = response['age']
print(response)
print(type(response))
print(age2)
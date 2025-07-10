import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

if response.status_code == 200:
    print("Sucess!")
    data = response.json()
    
    print("This is a Chuck Norris Joke")
    print(data['value'])

else:
    print("Error in the API request!")
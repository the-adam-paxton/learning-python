from urllib import request
import json

url = "https://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
data = r.read()
jsonData = json.loads(data)
# print(r.getcode())
# print(jsonData)

class Joke:
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self):
        return f"Setup: {self.setup}\nPunchline: {self.punchline}\n\n"


jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"I found {len(jokes)} jokes")

for joke in jokes:
    print(joke)

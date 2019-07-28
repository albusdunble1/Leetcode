import colorama
import termcolor
import requests
import pyfiglet
import requests
from random import randint

colorama.init()

print(termcolor.colored(pyfiglet.figlet_format("Dad Joke 3000"), "magenta"))


joke_topic = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"

response = requests.get(url, 
    headers={"Accept": "application/json"}, 
    params= {
        "term": joke_topic
    }
)

data = response.json()

results = data['results']

if len(results) > 1:
    print(f"I've got {len(results)} jokes about {joke_topic}. Here's one:")
    random_joke = randint(0, len(results) - 1)
    print(results[random_joke]['joke'])
elif len(results) == 1:
    print(f"I've got {len(results)} joke about {joke_topic}. Here it is:")
    print(results[0]['joke'])
else:
    print(f"Sorry, I don't have any jokes for {joke_topic}! Please try again.")






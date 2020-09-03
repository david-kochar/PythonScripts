import requests
from random import choice
import pyfiglet

ascii_banner = pyfiglet.figlet_format("The Ultimate Dad Joke Generator!")
print(ascii_banner)

url = "https://icanhazdadjoke.com/search"

joke_topic = input("Let me tell you a Dad joke! What's your joke topic? ")

response = requests.get(
    url, headers={"Accept": "application/json"}, params={"term": joke_topic}
)

joke_list = [
    joke_dicts["joke"] for joke_dicts in response.json()["results"]
]  # build list of jokes from response

joke_count = len(joke_list)

if joke_count > 0:
    print(f"\nI've got {joke_count} joke(s) about {joke_topic}. Here's one:\n")
    print(choice(joke_list) + "\n")  # randomly select joke
else:
    print(f"Sorry, I don't have any jokes about {joke_topic}!\n")

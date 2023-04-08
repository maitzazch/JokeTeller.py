# joke_teller.py

import pyttsx3
import requests
import random
import json

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = json.loads(response.text)
    setup = data["setup"]
    punchline = data["punchline"]
    return setup, punchline

def tell_joke():
    setup, punchline = get_joke()
    engine = pyttsx3.init()
    engine.say(setup)
    engine.say(punchline)
    engine.runAndWait()

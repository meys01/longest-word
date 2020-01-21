import random
import string
import requests
import json

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, a_string):
        data = {}
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/:{a_string}")
        data = r.json()
        return data['found']

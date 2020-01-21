import random
import string
import requests
import json

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def random_grid():
        pass

    def is_valid(self, word):
        if not word:
            return False

        letters = self.grid.copy() # Consume letters from the grid

        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        return self.__check_dictionary(word)


    def __check_dictionary(self, word):
        data = {}
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        data = r.json()
        return data['found']

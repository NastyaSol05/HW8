import json
import os
import random


def open_file():
    with open(os.path.join('question.json')) as file:
        return json.load(file)


def random_question():
    qwe = open_file()
    return qwe[random.randint(0, 5)]

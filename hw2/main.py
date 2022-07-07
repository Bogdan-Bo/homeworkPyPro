import random
import string

import pandas as pd
from faker import Faker
from flask import Flask

app = Flask(__name__)
fake = Faker('ru_RU')


@app.route('/password')
def generator_password():
    password_gen = ''
    length = random.randint(10, 20)
    for i in range(length):
        password_gen += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation)

    return password_gen


@app.route('/csv')
def get_avarage_parametrs():
    dataset = pd.read_csv('hw.csv')
    avarage = dataset.mean()
    return (
        f'Avarage Height: {round(avarage[" Height(Inches)"], 2)}, '
        f'Avarage Weight: {round(avarage[" Weight(Pounds)"])}'
    )

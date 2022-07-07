import random
import string
import csv
import pandas as pd
import numpy as np
import requests
from database_handler import execute_query
import string

from faker import Faker
from flask import Flask, render_template, url_for

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
    return f'Avarage Height: {avarage.values[1:2]}, Avarage Weight: {avarage.values[2:1]}'

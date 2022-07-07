import random
import string
import csv
import pandas as pd
import numpy as np
import requests
from database_handler import execute_query

from faker import Faker
from flask import Flask, render_template, url_for


app = Flask(__name__)
fake = Faker('ru_RU')


@app.route('/')
def hello_world():  # put application's code here
    return 'hello'


@app.route('/about')
def about():
    return 'Information About!'


@app.route('/password')
def generator_password():
    password_gen = ''
    length = random.randint(10, 20)
    for i in range(length):
        password_gen += random.choice(string.ascii_lowercase + string.ascii_uppercase + '1234567890/@!#$%^&*()_+')

    return password_gen


@app.route('/csv')
def get_avarage_parametrs():
    dataset = pd.read_csv('hw.csv')
    avarage = dataset.mean()
    return f'Avarage Height: {avarage.values[1:2]}, Avarage Weight: {avarage.values[2:1]}'


@app.route('/students/<int:amount>')
def generator_students(amount):
    students = pd.DataFrame([{
        'name': fake.name(),
        'city': fake.city(),
        'email': fake.email(),
        'password': fake.password(),
        'date_of_birth': fake.date_of_birth(),

    }])
    students.to_csv('students.csv')
    get_students = render_template('students.csv')

    return str(get_students)


@app.route('/get_customers')
def get_customers():
    query = 'SELECT * FROM customers'

    records = execute_query(query)
    return records
print('hello World')

if __name__ == '__main__':
    app.run(debug=True)

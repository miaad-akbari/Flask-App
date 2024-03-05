import json
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
DATABASE_NAME = 'cities.db'


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS cities (name TEXT, temperature REAL, humidity REAL)')
    conn.commit()
    conn.close()


def fetch_city_data(city_name):
    with open('cities.json') as json_file:
        data = json.load(json_file)
        cities = data['cities']
        for city in cities:
            if city['name'] == city_name:
                return city['temperature'], city['humidity']
    return None


def insert_city_data(city_name, temperature, humidity):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO cities VALUES (?, ?, ?)', (city_name, temperature, humidity))
    conn.commit()
    conn.close()


@app.route('/tehran')
def get_tehran_data():
    city_name = "Tehran"
    temperature, humidity = fetch_city_data(city_name)
    
    if temperature is None or humidity is None:
        return jsonify({'error': 'City data not found'}), 404
    
    insert_city_data(city_name, temperature, humidity)
    return jsonify({'city': city_name, 'temperature': temperature, 'humidity': humidity})


if __name__ == '__main__':
    create_database()
    app.run(host='0.0.0.0')

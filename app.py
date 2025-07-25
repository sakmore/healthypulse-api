from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Health Monitoring API!"
@app.route('/vitals')
def get_vitals():
    vitals = {
        'heart_rate': random.randint(60, 100),
        'blood_pressure': f"{random.randint(90, 120)}/{random.randint(60, 80)}",
        'temperature': round(random.uniform(97.0, 99.5), 1),
        'spo2': random.randint(95, 100)
    }
    return jsonify(vitals)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/monitor')
def monitor():
    data = {
        "device_id": "Device001",
        "status": "Active",
        "suspicious": random.choice([True, False])
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

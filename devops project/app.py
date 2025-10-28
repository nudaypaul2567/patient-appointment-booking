from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__,
            static_folder='.',
            static_url_path='')
CORS(app)

APPOINTMENTS_FILE = 'appointments.json'

def load_appointments():
    if os.path.exists(APPOINTMENTS_FILE):
        with open(APPOINTMENTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_appointments(appointments):
    with open(APPOINTMENTS_FILE, 'w') as f:
        json.dump(appointments, f, indent=2)

@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = load_appointments()
    return jsonify(appointments)

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()

    if not all(key in data for key in ['patientName', 'doctor', 'date', 'time']):
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate date is not in the past
    appointment_datetime = datetime.strptime(f"{data['date']} {data['time']}", '%Y-%m-%d %H:%M')
    if appointment_datetime < datetime.now():
        return jsonify({'error': 'Cannot book appointments in the past'}), 400

    appointments = load_appointments()

    # Check for conflicts (same doctor, date, time)
    for apt in appointments:
        if (apt['doctor'] == data['doctor'] and
            apt['date'] == data['date'] and
            apt['time'] == data['time']):
            return jsonify({'error': 'Time slot already booked'}), 409

    appointment = {
        'id': len(appointments) + 1,
        'patientName': data['patientName'],
        'doctor': data['doctor'],
        'date': data['date'],
        'time': data['time'],
        'created_at': datetime.now().isoformat()
    }

    appointments.append(appointment)
    save_appointments(appointments)

    return jsonify(appointment), 201

@app.route('/')
def serve_frontend():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

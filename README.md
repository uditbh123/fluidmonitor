# Fluid Monitor Dashboard 🧪

A Django web app for logging and visualizing industrial fluid sensor readings.
Built as a learning project to prepare for a backend developer role.

## Features
- Log sensor readings (pH, temperature, concentration)
- Bootstrap 5 responsive dashboard
- Live chart visualization with Chart.js
- Filter readings by sensor name
- Stats: average, min, max values

## Tech Stack
Python · Django · SQLite · Bootstrap 5 · JavaScript · Chart.js

## Setup
```bash
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Then open http://127.0.0.1:8000
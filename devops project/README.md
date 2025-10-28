# Patient Appointment Booking System

A simple web application for booking patient appointments with doctors.

## Features

- Book appointments with available doctors
- View list of booked appointments
- RESTful API backend
- Docker containerization
- CI/CD pipeline with GitHub Actions

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Database:** JSON file storage
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

## Setup and Installation

### Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://localhost:5000`

### Docker

1. Build the Docker image:
   ```bash
   docker build -t patient-appointment-booking .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 patient-appointment-booking
   ```

## API Endpoints

- `GET /appointments` - Get all appointments
- `POST /appointments` - Create a new appointment

## CI/CD

The project includes a GitHub Actions workflow that:
- Runs tests on push and pull requests
- Builds and pushes Docker images
- Deploys to the configured server

## Project Structure

```
.
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── index.html           # Frontend HTML
├── styles.css           # Frontend styles
├── script.js            # Frontend JavaScript
├── .github/workflows/   # CI/CD workflows
│   └── ci-cd.yml
└── README.md            # This file

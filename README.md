\documentclass[a4paper,12pt]{article}
\usepackage{geometry}
\geometry{margin=1in}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{setspace}
\usepackage{titlesec}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
}

\title{\textbf{Patient Appointment Booking System}}
\author{Developed using Flask and Python}
\date{\today}

\begin{document}
\maketitle
\onehalfspacing

\section*{Overview}
The \textbf{Patient Appointment Booking System} is a simple web-based API built using \textbf{Flask (Python)} that allows patients to book appointments with doctors. It provides endpoints for retrieving and creating appointments while validating conflicts and ensuring that appointments cannot be scheduled in the past.

\section*{Features}
\begin{itemize}
    \item RESTful API endpoints for appointment management.
    \item Supports \texttt{GET} and \texttt{POST} methods.
    \item Prevents booking appointments in the past.
    \item Detects time-slot conflicts for the same doctor.
    \item Stores appointment data in a local \texttt{appointments.json} file.
    \item CORS-enabled for cross-origin access.
\end{itemize}

\section*{Project Structure}
\begin{verbatim}
patient-appointment-booking/
│
├── app.py
├── appointments.json      # Stores appointment data
├── index.html             # (Optional) Frontend interface
└── README.tex             # Project documentation
\end{verbatim}

\section*{Installation and Setup}
\begin{enumerate}
    \item Install Python (version 3.8 or higher).
    \item Install the required dependencies:
    \begin{verbatim}
    pip install flask flask-cors
    \end{verbatim}
    \item Run the application:
    \begin{verbatim}
    python app.py
    \end{verbatim}
    \item Open your browser and navigate to:
    \begin{verbatim}
    http://localhost:5000
    \end{verbatim}
\end{enumerate}

\section*{API Endpoints}
\subsection*{1. GET /appointments}
\textbf{Description:} Retrieves all existing appointments.

\textbf{Response Example:}
\begin{verbatim}
[
  {
    "id": 1,
    "patientName": "John Doe",
    "doctor": "Dr. Smith",
    "date": "2025-11-02",
    "time": "10:30",
    "created_at": "2025-10-28T14:22:35.123456"
  }
]
\end{verbatim}

\subsection*{2. POST /appointments}
\textbf{Description:} Creates a new appointment.

\textbf{Request Body:}
\begin{verbatim}
{
  "patientName": "John Doe",
  "doctor": "Dr. Smith",
  "date": "2025-11-02",
  "time": "10:30"
}
\end{verbatim}

\textbf{Possible Responses:}
\begin{itemize}
    \item \texttt{201 Created} - Appointment successfully created.
    \item \texttt{400 Bad Request} - Missing or invalid fields.
    \item \texttt{409 Conflict} - Time slot already booked.
\end{itemize}

\section*{Backend Logic Overview}
\begin{itemize}
    \item Appointments are read and written from a local JSON file.
    \item When a new booking request is made, the system:
    \begin{enumerate}
        \item Validates required fields (\texttt{patientName}, \texttt{doctor}, \texttt{date}, \texttt{time}).
        \item Ensures the appointment date/time is in the future.
        \item Checks for doctor time-slot conflicts.
        \item Saves valid appointments to \texttt{appointments.json}.
    \end{enumerate}
\end{itemize}

\section*{Example Usage}
\begin{enumerate}
    \item Send a POST request to \texttt{/appointments} using tools like \textbf{Postman} or \textbf{curl}:
    \begin{verbatim}
    curl -X POST http://localhost:5000/appointments \
    -H "Content-Type: application/json" \
    -d '{"patientName":"Alice","doctor":"Dr. Brown",
         "date":"2025-11-05","time":"09:00"}'
    \end{verbatim}
    \item Retrieve all appointments:
    \begin{verbatim}
    curl http://localhost:5000/appointments
    \end{verbatim}
\end{enumerate}

\section*{Future Enhancements}
\begin{itemize}
    \item Add database integration (e.g., SQLite or MongoDB).
    \item Implement user authentication and authorization.
    \item Add appointment cancellation and update endpoints.
    \item Build a frontend dashboard for doctors and patients.
\end{itemize}

\section*{License}
This project is open-source and available under the \textbf{MIT License}.

\end{document}

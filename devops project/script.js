document.getElementById('appointmentForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const patientName = document.getElementById('patientName').value;
    const doctor = document.getElementById('doctor').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    const appointment = {
        patientName,
        doctor,
        date,
        time
    };

    try {
        const response = await fetch('/appointments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(appointment)
        });

        if (response.ok) {
            document.getElementById('appointmentForm').reset();
            displayAppointments();
            alert('Appointment booked successfully!');
        } else {
            const error = await response.json();
            alert(`Error: ${error.error}`);
        }
    } catch (error) {
        console.error('Error booking appointment:', error);
        alert('Error booking appointment. Please try again.');
    }
});

async function displayAppointments() {
    try {
        const response = await fetch('/appointments');
        const appointments = await response.json();

        const appointmentsList = document.getElementById('appointmentsList');
        appointmentsList.innerHTML = '';

        appointments.forEach(appointment => {
            const li = document.createElement('li');
            li.textContent = `${appointment.patientName} - ${appointment.doctor} - ${appointment.date} at ${appointment.time}`;
            appointmentsList.appendChild(li);
        });
    } catch (error) {
        console.error('Error loading appointments:', error);
    }
}

// Display appointments on page load
displayAppointments();

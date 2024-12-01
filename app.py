from flask import Flask, request, render_template
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'kaviyah460@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'jfpp gooo asvo hylc'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = 'kaviyah460@gmail.com'  # Your email

mail = Mail(app)

@app.route('/')
def simple():
    return render_template('simple.html')  # Create this file next
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']
    guests = request.form['guests']
    special_requests = request.form['special-requests']

    # Create the email content
    subject = "Reservation Confirmation at Savory Delight"
    message = f"""Dear {name},

Thank you for your reservation at Savory Delight!

Here are your reservation details:
Date: {date}
Time: {time}
Number of Guests: {guests}
Special Requests: {special_requests}

We look forward to welcoming you!

Best regards,
Savory Delight Team
"""
    # Send the email
    msg = Message(subject, recipients=[email])
    msg.body = message
    mail.send(msg)

    return "Reservation submitted successfully. A confirmation email has been sent."


@app.route('/submit-job-application', methods=['POST'])
def submit_job_application():
    # Extract form data
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    position = request.form['position']
    experience = request.form['experience']
    education = request.form['education']
    skills = request.form['skills']
    availability = request.form['availability']

    # Email subject and body
    subject = "Application Received at Savory Delight"
    message_body = f"""
    Dear {name},

    Thank you for applying for the {position} position at Savory Delight. We have received your application.

    Here's the summary of your details:
    - Phone: {phone}
    - Position Applied For: {position}
    - Years of Experience: {experience}
    - Education: {education}
    - Skills: {skills}
    - Availability: {availability}

    Our HR team will review your application and get back to you soon.

    Best regards,
    Savory Delight HR Team
    """

    # Send the email
    msg = Message(subject, recipients=[email])
    msg.body = message_body
    mail.send(msg)

    return "Job application submitted successfully. A confirmation email has been sent."

if __name__ == '__main__':
    app.run(debug=True)

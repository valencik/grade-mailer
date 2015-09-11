from __future__ import print_function
import csv

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

me = "me@example.com"

# Read in Grades file
# ID,email,grade
reader = csv.reader(open("grades.csv", "rb"))
for row in reader:
    student_id = row[0]
    student_email = row[1]
    student_grade = int(row[2])

    # Check for NA email
    if student_email == 'NA':
        print("No email for {0}".format(student_id))
        continue

    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    if 0 < student_grade < 26:
        with open("fail-message.txt") as fp:
            # Create a text/plain message
            message = str(fp.read()).format(id=student_id, score=student_grade)
            msg = MIMEText(message)
    elif 26 <= student_grade <= 40:
        with open("pass-message.txt") as fp:
            # Create a text/plain message
            message = str(fp.read()).format(id=student_id, score=student_grade)
            msg = MIMEText(message)
    elif student_grade == 50:
        with open("null-message.txt") as fp:
            # Create a text/plain message
            message = str(fp.read()).format(id=student_id)
            msg = MIMEText(message)

    msg['Subject'] = "Hello, World!"
    msg['From'] = me
    msg['To'] = student_email

    # Send the message via our own SMTP server.
    print("Trying to send mail to {id} at {email}...".format(id=student_id, email=student_email))
    s = smtplib.SMTP('localhost')
    s.sendmail(me, student_email, msg.as_string())
    s.quit()

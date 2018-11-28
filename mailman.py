import getpass
import csv
import smtplib

def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

email = input("Email: ")
passwd = getpass.getpass("Password: ")

with open("format.content") as file: 
   format = file.readlines() # Thus format now contains the content as well as the subject of the mail(row 0)

# data.csv contains the details of all those receiving the email. The format is given below
"""
Name, Email, Extra (Details of no particular reason here)
"""
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Below, each row contains the details of a user
    for row in csv_reader:
        mentor = mentor_contact[row[2]]
        print(f'Email sent to {row[0]} @ email {row[1]})
        sub = format[0]
        body = "".join(format[1:]).replace("{Name}", row[0]) # Take in body of email from content file and make manipulate it according to reciever.
        email = row[1] # The email of the reciever
        send_email(email, passwd, recipient, sub, body)
        server.quit()
             


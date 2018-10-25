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

mentor_contact = {}
with open('mentors.csv') as mentors_csv:
    for mentor_list in csv.reader(mentors_csv, delimiter=','):
        mentor_contact[mentor_list[3]] = mentor_list[:3]

format = ""

with open("format.content") as file: 
   format = file.readlines()



with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        mentor = mentor_contact[row[2]]
        print(f'Email sent to {row[0]} @ email {row[1]} allotted to {", ".join(mentor)}')
        sub = format[0]
        body = "".join(format[1:])
        email = "devdutt@ieee.org" #row
        body = body.replace("{Name}", row[0]).replace("{mentor_name}", mentor[0]).replace("{mentor_phone}", mentor[2]).replace("{mentor_email}", mentor[1])
        print(body)
        send_email(email, passwd, email, sub, body)


# FOSSMEC mailer.py
The opensource script for emailing stuff, built for FOSSMEC by FOSSMEC!

This is a nifty Python Script that can send batch mails to people as mentioned in the data.csv file. It can also take in the content it needs from format.content file. This includes HTML syntax and converts it into an email by sending it through a SMTP pipeline. Password and username of the account that is used in the process of sending the email are set at the time of emailing. We use getpass module to do the same, though it is not strictly important.

## Format of data.csv
The data.csv file contains the details of those receiving  the email. As per the requirements, we are supposed to use the following structure when making this particular file.

```csv
Name of Reciever, reciever@email, <Extra details that maybe irrelevant>
```

## Format of format.content
This file contains the content of the email. The first line is the subject line whereas the rest is body, body can be HTML as depicted underneath.
```html
Subject Line Goes Like This
<!Doctype>
<Add your HTML here>
```
## Libraries  used
The only external module used in this script is the **smtplib** library. It defines an smtp client session object, which can be used to send emails to any internet machine with **SMTP** OR **ESMTP** listener daemons.

## Running the script 
The **smtplib** library is a prerequisite  for running this script, along with a stable internet connection. Create(or modify) *format.content* file containing the **HTML EMAIL** format and the *data.csv* within the same directory. Run the script with Python 3x. 

## Input
The inputs from the user are in the form of an authentication for the email account through which the mails are sent. Herein the getpass function of python is used to receive the password in redacted format.

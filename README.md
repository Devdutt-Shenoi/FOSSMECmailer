# FOSSMEC mailer.py
The opensource script for emailing stuff, built for FOSSMEC by FOSSMEC!

This is a nifty Python Script that can send batch mails to people as mentioned in the data.csv file. It can also take in the content it needs from format.content file. This includes HTML syntax and convert it into an email by sending it through a SMTP pipeline. Password and username of the account that is used in the process of sending the email is set at time of emailing. we use getpass module to do the same, though it is not strictly important.

## Format of data.csv
The data.csv file contains the detials of those recieving the email. As per the requirements we are supposed to use the following structure when making this particular file.

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
## Librariers used
The only external module used in this script is the **smtplib** library which defines an smtp client session object which can be then used for sending emails to any internet machine with **SMTP** OR **ESMTP** listener daemon.

## Running the script 
Your require **smtplib** library as a prerequiste for running this script along with a stable internet connection. Create(or modify if required) format.content file of **HTML EMAIL** format and data.csv within the same directory.Run the script with python 3.7. 

## Input
The email id and password of the user who runs the script,from whom all the mails are to be sent is taken.With password taken in securely using the getpass function of python.

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

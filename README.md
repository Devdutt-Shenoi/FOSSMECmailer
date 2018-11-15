# FOSSMEC mailer.py
The opensource script for emailing stuff, built for FOSSMEC by FOSSMEC!

This is a nifty Python Script that can send batch mails to people as mentioned in the data.csv file. It can also take in the content it needs from format.content file. This includes HTML syntax and convert it into an email by sending it through a SMTP pipeline. Password and username of the account that is used in the process of sending the email is set at time of emailing. we use getpass module to do the same, though it is not strictly important.

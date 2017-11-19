# -*- coding: utf-8 -*-
#vbmusvjodyfbwksx

import smtplib
import sys

def send_email(recipient, subject, body): 

    gmail_user = "safesfabio@gmail.com"
    gmail_pwd = "vbmusvjodyfbwksx"
    FROM = gmail_user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        # SMTP_SSL Example
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)  
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
        server_ssl.sendmail(FROM, TO, message)
        #server_ssl.quit()
        server_ssl.close()
        print ('successfully sent the mail')
    except:
     print("Unexpected error:", sys.exc_info()[0])
     raise
        
#send_email("safesfabio@gmail.com", "Hallo!", "Deine Nummer  diese Woche lauten: ")
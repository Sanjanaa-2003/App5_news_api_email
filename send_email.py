import os
import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sanjanaarj2003@gmail.com"
    password = "sikf lhds pynp oave"
    #Google account--Security--App passwords--copypaste

    receiver = "sanjanaarj2003@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

#To create an app password:
# 1.Google account -- Security -- 2 step authentication -- App passwords -- Create a new one for this app
#  -- Paste it in the password variable in the code

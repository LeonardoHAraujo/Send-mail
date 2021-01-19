import PySimpleGUI as sg
from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Send_mail():

    def __init__(self):
        layout = [
            [sg.Text('To'), sg.Input()],
            [sg.Text('Subject'), sg.Input()],
            [sg.Text('Message'), sg.Input()],
            [sg.Button('send data')]
        ]

        window = sg.Window('Send Mail').layout(layout)
        self.button, self.values = window.Read()

        self.send_mail(self.values[0], self.values[1], self.values[2])

    def send_mail(self, to, subject, msg):
        # Configuration
        host = 'smtp.gmail.com'
        port = 587
        user = '<seu-email@gmail.com>'
        password = '<SENHA>'

        # Create object
        server = smtplib.SMTP(host, port)

        # Login with server
        server.ehlo()
        server.starttls()
        server.login(user, password)

        # Create menssage
        message = msg

        email_msg = MIMEMultipart()
        email_msg['From'] = user
        email_msg['To'] = to
        email_msg['Subject'] = subject
        email_msg.attach(MIMEText(message, 'plain'))

        # Send menssage
        server.sendmail(user, to, email_msg.as_string())
        print('Mensagem enviada!')
        server.quit()

mail = Send_mail()

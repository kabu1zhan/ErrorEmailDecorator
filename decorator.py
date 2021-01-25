from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, traceback, os


def send_error_to_email_decorator(function):
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    login = os.getenv("EMAIL")
    password = os.getenv('PASSWORD')
    print(login, password)
    server.login(login, password)

    def the_wrapper_around_the_original_function():
        try:
            function()
        except:
            error = traceback.format_exc()
            print(error)
            msg = MIMEMultipart('alternative')

            message = 'Вылезла ошибка'
            msg['From'] = 'kabiljanz0301@gmail.com'
            msg['To'] = 'kabiljanz0301@gmail.com'
            msg['Subject'] = 'Отчет об ошибках'

            msg.attach(MIMEText(message, 'plain'))
            msg.attach(MIMEText(error, 'plain'))

            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            print('Succes send mail to %s' % (msg['To']))
    return the_wrapper_around_the_original_function

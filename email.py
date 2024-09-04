import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# Email settings
SMTP_SERVER = 'smtp.your-email-provider.com'
SMTP_PORT = 587
SMTP_USER = 'thiagospam1299@gmail.com'
SMTP_PASS = 'localhost'

def send_email():
    sender_email = 'thiagospam1299@gmail.com'
    receiver_email = 'juliana.tiete@cognyte.com'
    subject = 'Lembrete: Comprovação de trabalho'
    body = 'Olá, tudo bem?\n\nHá uma previsão de prazo para o envio das comprovações de trabalho. Esse é o último documento que preciso.\n\nA comprovação de experiência é necessária para a extensão da minha permanência no Canadá.\n\nAgradeço desde já pela atenção e ajuda.'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        server.quit()

# Schedule the email to be sent daily
schedule.every().day.at("08:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)

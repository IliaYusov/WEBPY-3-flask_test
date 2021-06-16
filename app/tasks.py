import smtplib
from email.message import EmailMessage
from app import app
from celery import Celery

celery = Celery(
    'app',
    backend='redis://localhost:6379/13',
    broker='redis://localhost:6379/14',
)

celery.conf.update(app.config)


class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)


celery.Task = ContextTask


@celery.task
def celery_send_email(users):
    gmail_user = 'email'
    gmail_password = 'password'

    for user in users:
        msg = EmailMessage()
        msg['From'] = gmail_user
        msg['To'] = user['email']
        msg['Subject'] = 'OMG Super Important Message'
        msg.set_content(
            f"Добрый день, {user['username']}. Спасибо, что пользуетесь нашим сервисом объявлений."
        )

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.send_message(msg)
            server.close()

        except smtplib.SMTPException:
            return f'Something went wrong on {user["email"]}'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()


class NotificationService:

    @staticmethod
    def send_email(subject, message):

        sender = os.getenv("EMAIL_ADDRESS")
        password = os.getenv("EMAIL_PASSWORD")
        receiver = os.getenv("RECEIVER_EMAIL")

        msg = MIMEMultipart()

        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        try:

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender, password)

            server.sendmail(
                sender,
                receiver,
                msg.as_string()
            )

            server.quit()

            return True

        except Exception as e:

            print(e)
            return False
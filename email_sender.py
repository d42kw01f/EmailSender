from email.message import EmailMessage
import imghdr
import smtplib, ssl, os

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = os.environ['EMAIL_ADD']
        self.password = os.environ['EMAIL_PASS']

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        
        for email in emails:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = self.sender_mail
            msg['To'] = email
            msg.set_content(content)

            with open('/mnt/c/Users/pdaks/Downloads/CVs/Dakshitha_Perera.pdf', 'rb') as f:
                file_data = f.read()
                file_name = f.name
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            result = service.sendmail(self.sender_mail, email, msg.as_string())

        service.quit()


if __name__ == '__main__':
    mails = input("Enter emails: ").split()
    subject = input("Enter subject: ")
    content = input("Enter content: ")

    mail = Mail()
    mail.send(mails, subject, content)

import smtplib


class Email:
    def __init__(self):
        self.conn = smtplib.SMTP('smtp.gmail.com', 587)
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.login(USERNAME)


if __name__ == '__main__':
    e = Email()

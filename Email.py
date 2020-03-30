import smtplib

from ENV.SECRET import USERNAME, PASSWORD


class Email:
    def __init__(self):
        self.conn = smtplib.SMTP('smtp.gmail.com', 587)
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.login(USERNAME, PASSWORD)
        self.conn.sendmail(USERNAME, USERNAME, 'Subject:So long...\n\nDear Aviral, here is a test email.\n\n-Aviral')
        self.conn.quit()


if __name__ == '__main__':
    e = Email()

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass


class sendClass():
    username = None
    host = "smtp.gmail.com"
    port = 587
    from_email = username
    to_email = None
    plain_txt = None
    e_conn = None

    def set_Conn():
        try:
            print("Connecting!")
            sendClass.e_conn = SMTP(sendClass.host, sendClass.port)
            print(sendClass.e_conn.ehlo())
            print(sendClass.e_conn.starttls())
            # password = input("Enter the password: ")
            password = getpass.getpass(prompt="Enter your password: ")
            print(sendClass.e_conn.login(sendClass.username, password))
            print("Connected to SMTP server!")

            # plain_txt = "This is a test message in plain!!"
        except:
            print("Error in login!")
        finally:
            print("Logged in!")

    def send_email():
        try:
            # print(sendClass.e_conn)
            print("Sending mail to", sendClass.to_email)
            the_msg = MIMEMultipart("alternative")
            the_msg['Subject'] = "Hello There!"
            # print(sendClass.username)
            the_msg['From'] = sendClass.username
            part1 = MIMEText(sendClass.plain_txt, "plain")
            # part2 = MIMEText(html_txt, "html")
            the_msg.attach(part1)
            # the_msg.attach(part2)

            sendClass.e_conn.sendmail(sendClass.username, sendClass.to_email,
                                      the_msg.as_string())
            print("Mail send!")
        except Exception as error:
            print("Error occurred!", error)
        finally:
            print("Done")

    def quit_email():
        try:
            print(sendClass.e_conn.quit())
            print("Connection closed successfully!")
        except:
            print("Error in quit!")

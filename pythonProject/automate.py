import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(name, email,SendingEmail,Password,EmailSubject):
    senderEmail = SendingEmail
    senderPass = Password
    subject = EmailSubject  # Use the global variable

    body ="""
    As a Duet Student Branch 
    member, you'll have access to a wide range of benefits, including:

1.Participation in our exciting events, workshops, and seminars.
2.Networking with fellow students and professionals.
3.Opportunities to showcase your skills and talents.
4.Access to valuable resources, publications, and technical content.

    We encourage you to explore our social media channels to stay updated on upcoming activities and get involved in the various projects and initiatives.

    Thank you for joining our community. We look forward to a productive and inspiring association with you.

Warm regards,

 IEEE Computer Society-DSB'''

    """

    message = MIMEMultipart()
    message["From"] = senderEmail
    message["To"] = email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(senderEmail, senderPass)
            server.sendmail(senderEmail, email, message.as_string())
            print("Email sent Successfully!")
    except Exception as err:
        print(f"Error sending email: {err}")

name = "hanzala"
email = ['''Certainly! Here are the emails enclosed in double inverted commas:

"''']
SenderEmail = ["wahidhanzala123@gmail.com"]
Password = ""
EmailSubject = "Welcome to the IEEE Computer Society-DSB"


send_email(name, email,SenderEmail,Password,EmailSubject)

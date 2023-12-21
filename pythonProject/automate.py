# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# def send_text_message(email, text_message):
#     # Email configuration
#     sender_email = "wahidhanzala123@gmail.com"
#     sender_password = "ngdp uznw lbzt cjcc"
#     subject = "Membership Confirmation"
#
#
# # Example usage
# email_address = ["mashoodmajid2414@gmail.com","ibadmoin@gmail.com"]
# text_message = '''Dear Member,
#
# We are thrilled to inform you that your membership with the IEEE Computer Society's Duet Student Branch has been successfully confirmed!
#
#     Welcome to our vibrant community of aspiring tech dreamers, curious researchers, and passionate technology enthusiasts! We're all here to explore, learn, and inspire each other in the ever-evolving world of technology. Your membership with us opens up a world of opportunities to learn, collaborate, and grow within the field of computer science and engineering.
#
# As a Duet Student Branch member, you'll have access to a wide range of benefits, including:
#
# 1.Participation in our exciting events, workshops, and seminars.
# 2.Networking with fellow students and professionals.
# 3.Opportunities to showcase your skills and talents.
# 4.Access to valuable resources, publications, and technical content.
#
#     We encourage you to explore our social media channels to stay updated on upcoming activities and get involved in the various projects and initiatives.
#
#     Thank you for joining our community. We look forward to a productive and inspiring association with you.
#
# Warm regards,
#
#  IEEE Computer Society-DSB'''
#     # Message setup
#     message = MIMEMultipart()
#     message["To"] = email
#     message["From"] = sender_email
#     message["Subject"] = subject
#
#     # Attach the text message
#     message.attach(MIMEText(text_message, "plain"))
#
#     # Connect to the SMTP server (for Gmail in this case)
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, email, message.as_string())
#
# send_text_message(email_address, text_message)
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
SenderEmail = "wahidhanzala123@gmail.com"
Password = "ngdp uznw lbzt cjcc"
EmailSubject = "Welcome to the IEEE Computer Society-DSB"


send_email(name, email,SenderEmail,Password,EmailSubject)

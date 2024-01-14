import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import base64



load_dotenv()

SendingEmail = os.environ.get("Email")
Password = os.environ.get("Password")
EmailSubject = os.environ.get("EmailSubject")
EmailBody = os.environ.get("EmailBody")



def send_email(name, email,certificate_path ):
    sender_email = SendingEmail
    sender_password = Password
    subject = EmailSubject



    body = f"""
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Email Title</title>
    <style>
        /* Add your custom styles here */
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }}

        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 10px;
        }}

        h1, h2, h3,h4,b, p {{
            margin-bottom: 20px;
            color:black !important;
           
        }}

        a {{
            color: #3498db;
        }}
        .icons{{
            display: flex;
            align-items: center;
            margin-top: 25px;
            gap: 19px;
        }}

    

    </style>
</head>

<body>
    <div class="container">
       <div style="display: flex; justify-content: space-between;align-items: center;">
        <h1>IEEE Computer Society-DSB</h1>
       
       </div>
       <div style="width: 100%;height: max-content;">
        <img style="width: 100%;" src="https://scontent-mxp1-1.xx.fbcdn.net/v/t39.30808-6/413867829_219875361164926_3356272826442090458_n.jpg?stp=dst-jpg_s600x600&_nc_cat=107&ccb=1-7&_nc_sid=dd5e9f&_nc_eui2=AeHtRdf-xf_4zXZ-s2tO3C3IjOiQB_yzAOCM6JAH_LMA4HvP_j4Gbz_GsdUkwUXoTfwld0Ta1IaaQ0h0znVEMD2Y&_nc_ohc=KELaXXXyEbUAX_fLtZJ&_nc_ht=scontent-mxp1-1.xx&oh=00_AfDtGc6x6RXua0vrnjQijUtNIRRUHHu0PPOJk0MTPtjamA&oe=658F39D8"  />
       </div>
       <div class="container1">
        <h4>Dear Participant,</h4>
        <p><b>{name}</b></p>
        <p>Thank you for attending the LinkedIn Masterclass organized by IEEE Computer Society. We appreciate your active participation.</p>

        <p>Attached to this email is your Certificate of Appreciation post it on your LinkedIn and don't forget to tag IEEE CS-DSB.</p>

        <p>Here is the Link Tree of IEEE Computer Society: <a href="https://linktr.ee/ieeecsdsb" target="_blank">https://linktr.ee/ieeecsdsb</a></p>

        <p>Speaker's LinkedIn Profile: <a href="https://www.linkedin.com/in/syasirulhaq/" target="_blank">https://www.linkedin.com/in/syasirulhaq/</a></p>

        <p>Thank you once again for your participation.</p>

        <p>Best regards,<br><b>IEEE Computer Society-DSB</b></p>

          <b>Connect With Us</b>
        <div class="icons" style="display:flex;align-items: center;width: 50%; justify-content:space-around; margin-top:5px; gap:19px;">
           <a href="https://www.facebook.com/IEEECSDUET" target="_blank"> <img style="margin:10px;width:30px;height:30px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVih4o5wiiLPPMnkahxjAmn5Dy4t-WfRQEkkSSYlSyw&s" style="width: 30px;"></a>
           <a href="https://www.instagram.com/ieeecomputersocietyduet/" target="_blank"> <img style="margin:10px;width:30px;height:30px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrWQcM1JaPcE-PLolkW0V-1bEJefYL2wUDknIvSL-jpw&s" style="width: 30px;"></a>
           <a href="https://www.linkedin.com/company/ieee-computer-society-duet/" target="_blank"> <img style="margin:10px;width:30px;height:30px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkNvO9a-Qu_gD5e3YNq80JmuCh…

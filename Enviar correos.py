## REVISAR CODIGO PARA ENVIAR CORREOS, NO ESTA FUNCIONADO.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_email = "forchuecristina0@gmail.com"
your_password = '6972 0945'  

message = MIMEMultipart()
message["From"] = your_email
message["To"] = recipient
message["Subject"] = "Email de prueba"  

body = "Prueba de email"
message.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email, recipient, message.as_string())
smtp_server.quit()
print("Enviado")


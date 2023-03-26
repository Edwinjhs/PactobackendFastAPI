# import smtplib
# from email.mime.text import MIMEText
# import requests
# import time

# # aqui puedes usar un correo de gmail el que vas a destinar para enviarte los correos
# sender_email = "zulmadirectv@gmail.com" 

# # aqui vas a configurar el correo receptor 
# receiver_email = "edwin.ejhnsn@gmail.com"

# # Aqui es la contraseña de aplicacion https://support.google.com/accounts/answer/185833?hl=es 
# app_password = "rubio1503"

# def check_website_status():
#     url = "http://127.0.0.1:8000/token/"
#     try:
#         response = requests.get(url)
#         return response.status_code == 200
#     except requests.exceptions.RequestException:
#         return False

# def send_email_notification():
#     message = MIMEText("La página está en línea.", "plain", "utf-8")
#     message["Subject"] = "Notificación: Página en línea"
#     message["From"] = sender_email
#     message["To"] = receiver_email

#     try:
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#             server.login(sender_email, app_password)
#             server.sendmail(sender_email, receiver_email, message.as_string())
#             print("Correo electrónico enviado correctamente.")
#     except Exception as e:
#         print(f"Error al enviar el correo electrónico: {e}")

# while True:
#     if check_website_status():
#         print("La página está en línea.")
#         send_email_notification()
#         break
#     else:
#         print("La página no está en línea. Reintentando en 1 minuto.")
#         time.sleep(60)
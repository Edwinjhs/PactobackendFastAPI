import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import FastAPI, Request
import sqlite3

reset_pw_router= FastAPI()

@reset_pw_router.post("/restablecer-contraseña")
async def restablecer_contraseña(request: Request):
    email = await request.json()
    
    # Consulta si el correo existe en la base de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email=?", (email,))
    result = cursor.fetchone()
    if result is None:
        return {"message": "No hemos encontrado el correo."}

    # Crea el mensaje que se enviará
    from_email = "zulmadirectv@gmail.com"
    to_email = email
    subject = "Restablecer contraseña"
    body = "Hola,\n\nAquí está su nueva contraseña: ABC123.\n\nSaludos,\nEl equipo de mi sitio web."

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    text = MIMEText(body)
    msg.attach(text)

    # Establece la conexión con el servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Inicia sesión en la cuenta de correo electrónico
    email_address = from_email
    password = "elcguyxdbrwwdlox"
    server.starttls()
    server.login(email_address, password)

    # Envía el correo electrónico
    server.sendmail(from_email, to_email, msg.as_string())

    # Cierra la conexión con el servidor SMTP
    server.quit()

    return {"message": "Se ha enviado un correo electrónico con una nueva contraseña."}
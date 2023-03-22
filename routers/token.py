# import random
# import string
# import smtplib
# from email.mime.text import MIMEText
from fastapi import  HTTPException, Depends,  APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta


import service.token as Token_service
from service.user import UserService as UserService
from schemas.user import User as UserSchema
from service.token import user_token as TokenService

token_router = APIRouter()

@token_router.post("/token/",tags=['token'])
    # print(form_data.username)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(UserService.get_db)):
    user = TokenService.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    # si la contraseña y usuario coincide se crea el token y se le da el tiempo de expiracion
    access_token_expires = timedelta(minutes=Token_service.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = TokenService.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return{"access_token": access_token, "token_type": "bearer"}

@token_router.get("/api/users/me",tags=['token'])
async def read_users_me(current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    return current_user
# obtiene el usuario actual

@token_router.get("/api/users/me/items/",tags=['token'])
async def read_users_me_items(current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
# obtiene los items del usuario actual


# ---------------- trying reset-password -------------------- #

# @token_router.post("/reset-password/",tags=['token'])
# async def reset_password(email: str, db: Session = Depends(UserService.get_db)):
#     user = db.query(UserSchema).filter(UserSchema.email == email).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
#     # Genera un token único y lo guarda en la base de datos
#     token = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
#     user.reset_password_token = token
#     db.commit()
    
#     # Envía un correo electrónico al usuario con el token único
#     # Aquí deberás agregar tu propia lógica para enviar el correo electrónico
#     send_reset_password_email(email, token)
    
#     return {"message": "Reset password email sent"}

# @token_router.post("/reset-password/token/",tags=['token'])
# async def reset_password_token(token_data: UserSchema, db: Session = Depends(UserService.get_db)):
#     user = db.query(UserSchema).filter(UserSchema.email == token_data.email).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#     # Verifica que el token sea válido
#     if user.reset_password_token != token_data.token:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid reset password token")
    
#     # Genera un nuevo hash de contraseña y lo guarda en la base de datos
#     hashed_password = TokenService.get_password_hash(token_data.new_password)
#     user.hashed_password = hashed_password
#     user.reset_password_token = None
#     db.commit()

#     return {"message": "Password reset successful"}

# def send_reset_password_email(email: str, token: str):
#     pass

# # Configuración del servidor SMTP
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# smtp_user = 'zulmadirectv@gmail.com'
# smtp_password = 'rubio1503'

# # Información del correo electrónico
# from_email = 'tu_correo_electronico'
# to_email = 'correo_electronico_del_usuario'
# subject = 'Restablecer contraseña'
# message = 'Hola, para restablecer tu contraseña sigue este enlace: https://miapp.com/restablecer-contraseña'

# # Creamos el objeto MIMEText con el mensaje
# msg = MIMEText(message)

# # Configuramos los campos del correo electrónico
# msg['From'] = from_email
# msg['To'] = to_email
# msg['Subject'] = subject

# # Conexión con el servidor SMTP y envío del correo electrónico
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.ehlo()
# server.starttls()
# server.login(smtp_user, smtp_password)
# server.sendmail(from_email, to_email, msg.as_string())
# server.quit()
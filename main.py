from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import time

# DATA BASE
from database import engine, Base, SessionLocal

# ROUTERS
from routers.user import user_router
from routers.token import token_router
from routers.post import post_router
from routers.comments import comment_router
from routers.type_actor import type_actor_router
from routers.city import city_router
from routers.country import country_router
from routers.departament import departament_router
from routers.contribution import contribution_router
from routers.contribution_text import contributiontext_router


from auto_db import create_type_actors, create_location, create_contributions



from middleware.middleware import middleware_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "PACTO con FastAPI"
app.version = "0.0.1"


# Configurar el middleware CORS
origins = [
    "http://localhost:3000",  
    # Agrega aquí el origen de tu aplicación de React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(post_router)
app.include_router(token_router)
app.include_router(comment_router)
app.include_router(type_actor_router)
app.include_router(city_router)
app.include_router(country_router)
app.include_router(departament_router)
app.include_router(contribution_router)
app.include_router(contributiontext_router)



app.include_router(middleware_router)
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup():
    # Crear las tablas en la base de datos
    Base.metadata.create_all(bind=engine)

    # Crear los tipos de actores por defecto
    with SessionLocal() as session:
        create_type_actors(session)
        create_location()
        create_contributions(session)
        

# middleware(solo se puede consumir en app:fastapi)
# es un paso intermedio, recibe la info primero, la procesa y luego si la envia. (se utiliza para mejorar el manejo)
@app.middleware("http")
async def add_process_time_header(request:Request, call_next):
# esto añade tiempo de procesamiento de la peticion
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"]= str(process_time)
    return response

@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>esto esta en el back, esta conectado si me lees en react</h1>')
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import time

# DATA BASE
from database import engine, Base

# ROUTERS
from routers.user import user_router
from routers.token import token_router
from routers.post import post_router
from routers.comments import comment_router
# from routers.comments import comment_router


from middleware.middleware import middleware_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "PACTO con FastAPI"
app.version = "0.0.1"


# Configurar el middleware CORS
origins = [
    "http://localhost:3000",  # Agrega aquí el origen de tu aplicación de React
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

# app.include_router(comment_router)
app.include_router(middleware_router)

Base.metadata.create_all(bind=engine)

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
    return HTMLResponse('<h1>esto esta en el back</h1>')
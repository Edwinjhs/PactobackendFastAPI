from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import time

# DATA BASE
from database import engine, Base

# ROUTERS
from routers.user import user_router
from routers.token import token_router
from middleware.middleware import middleware_router
app = FastAPI()
app.title = "PACTO con FastAPI"
app.version = "0.0.1"

app.include_router(user_router)
app.include_router(token_router)
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
    return HTMLResponse('<h1>Hello PACTO</h1>')

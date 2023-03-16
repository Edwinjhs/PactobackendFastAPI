from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

# DATA BASE
from database import engine, Base

# ROUTERS
from routers.user import user_router
from routers.token import token_router

app = FastAPI()
app.title = "PACTO con FastAPI"
app.version = "0.0.1"

app.include_router(user_router)
app.include_router(token_router)

Base.metadata.create_all(bind=engine)

@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>Hello PACTO</h1>')

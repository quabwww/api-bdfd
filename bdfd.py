from fastapi import FastAPI

# .\run.bat

app = FastAPI()

@app.get("/")
def read_root():
    return {"funcion": funcion, "texto": texo}

from fastapi import FastAPI

app = FastAPI()

@app.get("/api/bdfd/funcion/{funcion}/{texto}")
def read_root(funcion: str, texto: str = None):
    if texto is None:
        texto = "Nada proporcionado"
    
    return {"funcion": funcion, "texto": texto}

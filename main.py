from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from claude_connection import claude_summarize
from anthropic import AuthenticationError, APIConnectionError, APITimeoutError

app = FastAPI()

class Item(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/summarize")
async def summarize(item: Item):
    if not item:
        raise HTTPException(status_code=400, detail="Text is empty")
    try:
        resumen = await claude_summarize(item.text)
    except AuthenticationError:
        return {"error": "Fallo en la autenticación."}
    except APIConnectionError:
        return {"error": "Fallo en la conexión con la API."}
    except APITimeoutError:
        return {"error": "Se superó el tiempo límite de la solicitud."}
    except:
        return {"error": "Ocurrió un error inesperado."}
    return {"resumen": resumen}
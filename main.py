from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    return JSONResponse(content="ESTA ES UNA API MONTADA EN UN HOST DE PRUEBA")
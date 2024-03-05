from fastapi import FastAPI

from app import almere_afval

app = FastAPI()
app.include_router(almere_afval.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome"
    }


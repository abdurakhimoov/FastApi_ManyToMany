from fastapi import FastAPI
import uvicorn

from db.database import engine, Base
from api import movie_router, actor_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kinolar va Aktyorlar API",
    description="Many-to-Many munosabatli professional FastAPI loyihasi",
    version="1.0.0"
)

app.include_router(movie_router.router)
app.include_router(actor_router.router)

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Xush kelibsiz!",
        "docs": "API hujjatlari bilan tanishish uchun /docs sahifasiga o'ting"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
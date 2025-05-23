from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="OSINT Scanner API",
    description="API להרצת כלים לאיסוף מודיעין על דומיינים (OSINT)",
    version="1.0.0"
)

app.include_router(router)

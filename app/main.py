from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.core.database import engine

app = FastAPI(
    title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG
)


@app.get("/")
def root():
    return {"message": "Report Analyzer API is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/health/database")
def database_health_check():

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {"database": "connected", "status": "healthy"}

    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database connection failed")

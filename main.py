from fastapi import FastAPI

from app.routes.inventory import router as tracker

app = FastAPI(
    title="Coffee Tracker API",
    version="1.0.0",
    description="An API for tracking inventory of small coffee business.",
)

app.include_router(tracker)

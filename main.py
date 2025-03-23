import uvicorn
from contextlib import asynccontextmanager
from app.config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.books.views import router as book_router
from app.database import db_helper
from app.books.models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.HOST,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router, prefix="/books")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

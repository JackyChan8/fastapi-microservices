import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import auth
from src.core.config import settings


app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    terms_of_service=f'/{settings.TERMS_OF_SERVICE}',
    contact={
        "name": settings.CONTACT_NAME,
        "url": settings.CONTACT_URL,
        "email": settings.CONTACT_EMAIL,
    },
    docs_url=f"/{settings.DOCS_URL}",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

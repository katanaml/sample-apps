from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api_router import router

app = FastAPI(openapi_url='/api/v1/fibonacci/openapi.json', docs_url='/api/v1/fibonacci/docs')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(router, prefix='/api/v1/fibonacci')
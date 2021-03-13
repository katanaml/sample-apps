from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from invoiceservice.app.api.invoices import invoices
import invoiceservice.app.api.db as db

app = FastAPI(openapi_url='/api/v1/invoices/openapi.json', docs_url='/api/v1/invoices/docs')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.on_event("startup")
def startup():
    db.init_db()
    db.start_pool()

app.include_router(invoices, prefix='/api/v1/invoices')
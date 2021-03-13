from typing import List
from fastapi import APIRouter

from invoiceservice.app.api import db_manager
from invoiceservice.app.api.models import Invoice

invoices = APIRouter()

@invoices.get('/')
def test():
    return 'API is running'

@invoices.get('/all', response_model=List[Invoice])
def get_all_invoices():
    return db_manager.get_all_invoices()
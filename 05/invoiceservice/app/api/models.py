from pydantic import BaseModel

class Invoice(BaseModel):
    INVOICE_DATE: str
    INVOICE_NUMBER: str
    TOTAL: float

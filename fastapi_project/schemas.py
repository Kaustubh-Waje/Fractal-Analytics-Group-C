from pydantic import BaseModel

class InvoiceCreate(BaseModel):
    vendor: str
    amount: int
    status: str

from schemas import InvoiceCreate
from models import Invoice
from fastapi import FastAPI
from models import Base
from database import engine
from database import SessionLocal
from models import Invoice
from redis_client import redis_client
import json
app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

@app.get("/invoices")
def get_invoices():

    cached_data = redis_client.get("all_invoices")

    if cached_data:
        return json.loads(cached_data)

    db = SessionLocal()

    invoices = db.query(Invoice).all()

    result = []

    for invoice in invoices:
        result.append({
            "id": invoice.id,
            "vendor": invoice.vendor,
            "amount": invoice.amount,
            "status": invoice.status
        })

    db.close()

    redis_client.set(
        "all_invoices",
        json.dumps(result)
    )

    return result
@app.post("/invoices")
def create_invoice(invoice: InvoiceCreate):

    db = SessionLocal()

    new_invoice = Invoice(
        vendor=invoice.vendor,
        amount=invoice.amount,
        status=invoice.status
    )

    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    redis_client.delete("all_invoices")

    db.close()

    return {
        "message": "Invoice created successfully",
        "id": new_invoice.id
    }
@app.put("/invoices/{invoice_id}")
def update_invoice(invoice_id: int, invoice: InvoiceCreate):

    db = SessionLocal()

    existing_invoice = db.query(Invoice).filter(
        Invoice.id == invoice_id
    ).first()

    if not existing_invoice:
        db.close()
        return {"message": "Invoice not found"}

    existing_invoice.vendor = invoice.vendor
    existing_invoice.amount = invoice.amount
    existing_invoice.status = invoice.status

    db.commit()
    redis_client.delete("all_invoices")

    db.close()

    return {"message": "Invoice updated successfully"}
@app.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: int):

    db = SessionLocal()

    invoice = db.query(Invoice).filter(
        Invoice.id == invoice_id
    ).first()

    if not invoice:
        db.close()
        return {"message": "Invoice not found"}

    db.delete(invoice)
    db.commit()
    redis_client.delete("all_invoices")

    db.close()

    return {"message": "Invoice deleted successfully"}

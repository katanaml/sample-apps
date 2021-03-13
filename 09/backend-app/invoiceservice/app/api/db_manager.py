import invoiceservice.app.api.db as db

def get_all_invoices():
    data = db.fetch_all_invoices()

    return data
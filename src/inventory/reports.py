from inventory.store import repo
from datetime import datetime

def expiry_report():
    to_show = []
    today = datetime.today()
    for product in repo.products.values():
        if product["type"] == "Perishable":
            expiry_date = datetime.strptime(product["expiry"], "%d-%m-%Y")
            days_left = (expiry_date - today).days
            if days_left <= 7:
                to_show.append((product["sku"], product["pname"], days_left))
    return to_show

def paginate(products, page_size):
    page = []
    for product in products:
        page.append(product)
        if len(page) == page_size:
            yield page
            page = []
    if page:
        yield page

def inventory_value():
    total_value = 0
    for product in repo.products.values():
        total_value += product["stock"] * product["price"]
    return total_value
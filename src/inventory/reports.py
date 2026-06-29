from inventory.store import repo
from datetime import datetime

def expiry_report():
    result = []
    today = datetime.today()
    for product in repo.products.values():
        if product["type"] == "Perishable":
            expiry_date = datetime.strptime(product["expiry"], "%d-%m-%Y")
            days_left = (expiry_date - today).days
            if days_left <= 7:
                result.append((product["sku"], product["pname"], f"Days Left: {days_left}"))
    return result

def low_stock_report(threshold=10):
    result = []
    for product in repo.products.values():
        if product["stock"] <= threshold:
            result.append((product["sku"], product["pname"], product["stock"]))
    return result

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
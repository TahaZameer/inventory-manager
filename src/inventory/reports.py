from inventory.store import repo

def inventory_value():
    total_value = 0
    for product in repo.products.values():
        total_value += product["stock"] * product["price"]
    return total_value
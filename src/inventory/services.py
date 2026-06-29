from inventory.store import repo, order_repo
from inventory.models import Product, Perishable, Order
from inventory.exceptions import ProductNotFoundError, DuplicateSKUError, InsufficientStock, InvalidAmountError, OrderStatusLocked

def add_product(price, sku, pname, stock, supplier):
    key = repo.find(sku)
    if key is not None:
        raise DuplicateSKUError()
    product = Product(price, sku, pname, stock, supplier)
    repo.add(product)
    repo.save()

def add_perishable(price, sku, pname, stock, supplier, expiry):
    key = repo.find(sku)
    if key is not None:
        raise DuplicateSKUError()
    product = Perishable(price, sku, pname, stock, supplier, expiry)
    repo.add(product)
    repo.save()

def delete_product(sku):
    repo.delete(sku)
    repo.save()

def find_product(sku):
    key = repo.find(sku)
    if key is None:
        raise ProductNotFoundError()
    return repo.products[key]

def list_products():
    return repo.products

def edit_product(sku, field, val):
    key = repo.find(sku)
    if key is None:
        raise ProductNotFoundError()
    data = dict(repo.products[key])
    data[field] = val
    product = Product.from_dict(data)
    repo.edit(sku, product)
    repo.save()

def dispatch_stock(sku, amount):
    key = repo.find(sku)
    if key is None:
        raise ProductNotFoundError()
    if amount < 1:
        raise InvalidAmountError()
    data = dict(repo.products[key])
    if data["stock"] - amount < 0:
        raise InsufficientStock()
    data["stock"] -= amount
    product = Product.from_dict(data)
    repo.edit(sku, product)
    repo.save()

def receive_stock(sku, amount):
    key = repo.find(sku)
    if key is None:
        raise ProductNotFoundError()
    if amount < 1:
        raise InvalidAmountError()
    data = dict(repo.products[key])
    data["stock"] += amount
    product = Product.from_dict(data)
    repo.edit(sku, product)
    repo.save()

def create_order():
    order = Order()
    order_id = order_repo.add(order)
    order_repo.save()
    return order_id

def add_to_order(order_id, sku, quantity):
    order_dict = order_repo.get(order_id)
    order = Order.from_dict(order_dict)
    if order.status != "unconfirmed":
        raise OrderStatusLocked()
    if repo.find(sku) is None:
        raise ProductNotFoundError()
    if quantity < 1:
        raise InvalidAmountError()
    order.add_item(sku, quantity)
    order_repo.edit(order_id ,order)
    order_repo.save()

def confirm_order(order_id):
    order = Order.from_dict(order_repo.get(order_id))
    if order.status != "unconfirmed":
        raise OrderStatusLocked()
    for sku, quantity in order.items.items():
        key = repo.find(sku)
        if key is None:
            raise ProductNotFoundError()
        product = repo.products[key]
        if quantity > product["stock"]:
            raise InsufficientStock()
    for sku, quantity in order.items.items():
        dispatch_stock(sku, quantity)
    order.status = "confirmed"
    order_repo.edit(order_id, order)
    order_repo.save()

def fulfil_order(order_id):
    order = Order.from_dict(order_repo.get(order_id))
    if order.status != "confirmed":
        raise OrderStatusLocked()
    order.status = "fulfilled"
    order_repo.edit(order_id, order)
    order_repo.save()

def cancel_order(order_id):
    order = Order.from_dict(order_repo.get(order_id))
    if order.status in ("cancelled", "fulfilled"):
        raise OrderStatusLocked()
    if order.status == "confirmed":
        for sku, quantity in order.items.items():
            receive_stock(sku, quantity)
    order.status = "cancelled"
    order_repo.edit(order_id, order)
    order_repo.save()

def view_order(order_id):
    order = order_repo.get(order_id)
    return order
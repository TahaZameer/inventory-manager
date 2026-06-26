from inventory.repository import Repository
from inventory.models import Product, Perishable
from inventory.exceptions import ProductNotFoundError, DuplicateSKUError, InsufficientStock, InvalidAmountError

repo = Repository()

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
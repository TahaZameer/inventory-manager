import json
from models import Product
from exceptions import ProductNotFoundError

class Repository:
    def __init__(self):
        try:
            with open("data/products.json") as f:
               data = json.load(f)
        except FileNotFoundError:
            data = {"version": 1,
                    "next_id": 1,
                    "products": {}}
        self.version = data["version"]
        self.next_id = data["next_id"]
        self.products = data["products"]

    def add(self, product):
        self.products[str(self.next_id)] = product.to_dict()
        self.next_id += 1

    def find(self, sku):
        for k, v in self.products.items():
            if v["sku"] == sku:
                return k
        return None
    
    def edit(self, sku, product):
        key = self.find(sku)
        if key is None:
            raise ProductNotFoundError()
        self.products[key] = product.to_dict()
    
    def delete(self, sku):
        key = self.find(sku)
        if key is None:
            raise ProductNotFoundError()
        del self.products[key]

    def save(self):
        with open("data/products.json", "w") as f:
            data = {"version": self.version,
                    "next_id": self.next_id,
                    "products": self.products}
            
            json.dump(data, f, indent=2)
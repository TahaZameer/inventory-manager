import json
import os
from pathlib import Path
from inventory.exceptions import ProductNotFoundError, CorruptDataError

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
DATA_FILE = DATA_DIR / "products.json"
TEMP_FILE = DATA_DIR / "products.tmp"

class Repository:
    def __init__(self):
        try:
            with open(DATA_FILE) as f:
               data = json.load(f)
        except FileNotFoundError:
            data = {"version": 1,
                    "next_id": 1,
                    "products": {}}
        except json.JSONDecodeError:
            raise CorruptDataError()
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

    #Making save atomic, prevents corruption of data if program crashes/closes during saving. data is either NEW or OLD
    def save(self):    
        data = {"version": self.version,
                    "next_id": self.next_id,
                    "products": self.products}
        
        with open(TEMP_FILE, "w") as f:
            json.dump(data, f, indent=2)

        os.replace(TEMP_FILE, DATA_FILE)
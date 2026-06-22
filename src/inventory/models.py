from inventory.validators import intCheck, LengthCheck, PresenceCheck, dateCheck

class Product:
    def __init__(self, price: int, sku: str, pname: str, stock: int, supplier: str):
        self.price = price
        self.sku = sku
        self.pname = pname
        self.stock = stock
        self.supplier = supplier

    @classmethod
    def from_dict(cls, data):
        typeProduct = data.pop("type")
        if typeProduct == "Product":
            return Product(**data)
        elif typeProduct == "Perishable":
            return Perishable(**data)
        
    def __repr__(self):
        return f"{self.__class__.__name__}(sku={self._sku}, product_name={self._pname}, supplier={self._supplier})"

    def to_dict(self):
        return {
            "price": self._price,
            "sku": self._sku,
            "pname": self._pname,
            "stock": self._stock,
            "supplier": self._supplier,
            "type": self.__class__.__name__
        }

    @property
    def cost(self):
        return f"{(self._price/100):.2f}"
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, val):
        if intCheck(val, canBeZero=False):
            self._price = val

    @property
    def sku(self):
        return self._sku
    
    @sku.setter
    def sku(self, val):
        if PresenceCheck(val) and LengthCheck(val):
            self._sku = val

    @property
    def pname(self):
        return self._pname
    
    @pname.setter
    def pname(self, val):
        if PresenceCheck(val):
            self._pname = val

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, val):
        if intCheck(val, canBeZero=True):
            self._stock = val

    @property
    def supplier(self):
        return self._supplier
    
    @supplier.setter
    def supplier(self, val):
        if PresenceCheck(val):
            self._supplier = val
            

class Perishable(Product):
    def __init__(self, price, sku, pname, stock, supplier, expiry):
        super().__init__(price, sku, pname, stock, supplier)
        self._expiry = expiry

    def __repr__(self):
        return f"{self.__class__.__name__}(sku={self._sku}, product_name={self._pname}, supplier={self._supplier}, expiry={self._expiry})"

    def to_dict(self):
        data = super().to_dict()
        data["expiry"] = self._expiry
        return data

    @property
    def expiry(self):
        return self._expiry
    
    @expiry.setter
    def expiry(self, val):
        if dateCheck(val):
            self._expiry = val
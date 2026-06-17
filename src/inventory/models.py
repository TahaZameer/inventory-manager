from validators import intCheck, LengthCheck, PresenceCheck

class Product:
    def __init__(self, price: int, sku: str, pname: str, stock: int, supplier: str):
        self.price = price
        self.sku = sku
        self.pname = pname
        self.stock = stock
        self.supplier = supplier

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
    def __init__(self, expiry: str):
        pass
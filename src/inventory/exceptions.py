class IntError(Exception):
    pass

class LengthError(Exception):
    pass

class PresenceError(Exception):
    pass

class FormatError(Exception):
    pass


class ProductNotFoundError(Exception):
    pass

class CorruptDataError(Exception):
    pass

class DuplicateSKUError(Exception):
    pass

class InsufficientStock(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class ItemNotInOrderError(Exception):
    pass

class OrderNotFoundError(Exception):
    pass
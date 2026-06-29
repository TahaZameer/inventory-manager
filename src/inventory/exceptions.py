class IntError(Exception):
    def __init__(self, message="Value Must Be A Whole Number, 0 or Greater"):
        super().__init__(message)

class LengthError(Exception):
    def __init__(self, message="SKU Must Be Exactly 5 Characters"):
        super().__init__(message)

class PresenceError(Exception):
    pass

class FormatError(Exception):
    pass


class ProductNotFoundError(Exception):
    def __init__(self, message="Product Not Found."):
        super().__init__(message)

class CorruptDataError(Exception):
    def __init__(self, message="The Data File Is Corrupt."):
        super().__init__(message)

class DuplicateSKUError(Exception):
    def __init__(self, message="SKU Already Exists."):
        super().__init__(message)

class InsufficientStock(Exception):
    def __init__(self, message="Not Enough Stock."):
        super().__init__(message)

class InvalidAmountError(Exception):
    def __init__(self, message="Amount Must Be A Positive Whole Number"):
        super().__init__(message)

class ItemNotInOrderError(Exception):
      def __init__(self, message="The Item Is Not In Order."):
        super().__init__(message)

class OrderNotFoundError(Exception):
    def __init__(self, message="The Order Does Not Exist."):
        super().__init__(message)

class OrderStatusLocked(Exception):
    def __init__(self, message="Action Is Not Allowed For The Order's Current Status."):
        super().__init__(message)
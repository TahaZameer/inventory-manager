from exceptions import IntError, PresenceError, LengthError, FormatError
from datetime import datetime

def intCheck(val, canBeZero):
    if isinstance(val, int):
        if canBeZero:
            if val >= 0:
                return True
            else:
                raise IntError("Value must be 0 or greater")
        if not canBeZero:
            if val > 0:
                return True
            else:
                raise IntError("Value must be greater than 0")
    else:
        raise IntError("Value must be an integer")

def PresenceCheck(val):
    if val == "":
        raise PresenceError("The field cannot be left empty")
    else:
        return True

def LengthCheck(val):
    if len(val) == 5:
        return True
    else:
        raise LengthError("The sku id must be exactly 5 characters")
    
def dateCheck(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        raise FormatError("The format must be, date-month-year, e.g 01-08-2026")
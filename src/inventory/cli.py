from inventory.services import add_product, add_perishable, list_products, delete_product, receive_stock, dispatch_stock, edit_product, find_product, create_order, add_to_order, confirm_order, fulfil_order, cancel_order, view_order
from inventory.reports import inventory_value, low_stock_report, expiry_report

def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def call_service(func, *arg):
    try:
        func(*arg)
    except Exception as e:
        print(f"Error: {e}")

def do_add_product():
    price = int_input("Price(in cents): ")
    sku = input("SKU(5 Characters): ")
    pname = input("Product Name: ")
    stock = int_input("Stock: ")
    supplier = input("Supplier: ")
    
    call_service(add_product, price, sku, pname, stock, supplier)

def do_add_perishable():
    price = int_input("Price(in cents): ")
    sku = input("SKU(5 Characters): ")
    pname = input("Product Name: ")
    stock = int_input("Stock: ")
    supplier = input("Supplier: ")
    expiry = input("Date(DD-MM-YYYY): ")
    
    call_service(add_perishable, price, sku, pname, stock, supplier, expiry)

def do_list_products():
    products = list_products()
    if not products:
        print("No Products yet.")
        return
    for product in products.values():
        price = product["price"] / 100
        print(f'{product["sku"]}, {product["pname"]}, ${price:.2f}, {product["stock"]} in stock')

def do_delete_product():
    sku = input("SKU: ")
    call_service(delete_product, sku)

def do_receive_stock():
    sku = input("SKU: ")
    stock_to_receive = int_input("Stock to Receive: ")
    call_service(receive_stock, sku, stock_to_receive)

def do_dispatch_stock():
    sku = input("SKU: ")
    stock_to_dispatch = int_input("Stock to Dispatch: ")
    call_service(dispatch_stock, sku, stock_to_dispatch)

def do_find_product():
    sku = input("SKU: ")
    try:
        product = find_product(sku)
        if product is None:
            print("Product Does Not Exist.")
        else:
            price = product["price"]
            result = (f'Name: {product["pname"]}, SKU: {product["sku"]}, Stock: {product["stock"]}, Price: ${price/100:.2f}, Type: {product["type"]}')
            if product["type"] != "Perishable":
                print(result)
            else:
                print(result + f', Expiry: {product["expiry"]}')
    except Exception as e:
        print(f"Error: {e}")


def do_edit_product():

    fields = {"1": "price",
          "2": "pname",
          "3": "stock",
          "4": "supplier"}
    
    sku = input("SKU: ")

    for key, value in fields.items():
        print(f"{key}: {value}")

    while True:
        field = input("Choose Field To Edit: ")
        if field not in fields:
            print("Choose a valid option")
        else:
            field = fields[field]
            break
    
    if field in ("stock", "price"):
        value = int_input("Edited Value: ")
    else:
        value = input("Edited Value: ")

    call_service(edit_product, sku, field, value)

def do_create_order():
    order_id = create_order()
    print(f"Order successfully created, Order ID = {order_id}")
    
def do_add_to_order():
    order_id = input("Order ID: ")
    sku = input("SKU: ")
    quantity = int_input("Quantity: ")

    call_service(add_to_order, order_id, sku, quantity)

def do_confirm_order():
    order_id = input("Order ID: ")
    call_service(confirm_order, order_id)

def do_fulfil_order():
    order_id = input("Order ID: ")
    call_service(fulfil_order, order_id)

def do_cancel_order():
    order_id = input("Order ID: ")
    call_service(cancel_order, order_id)

def do_view_order():
    order_id = input("Order ID: ")
    try:    
        order = view_order(order_id)
        print(f"Status: {order['status']}")
        for sku, quantity in order["items"].items():
            print(f'SKU: {sku}, Quantity: {quantity}')
    except Exception as e:
        print(f"Error: {e}")

def do_inventory_value():
    result = inventory_value()
    print(f"Total Inventory Value: ${result/100:.2f}")

def do_low_stock_report():
    report = low_stock_report()
    for sku, name, stock in report:
        print(f'SKU: {sku}, Name: {name}, Stock: {stock}')

def do_expiry_report():
    report = expiry_report()
    print(report)

labels = {"1": "Add a Product",
           "2": "Add a Perishable Product",
           "3": "Edit a Product",
           "4": "Delete a Product",
           "5": "List Products",
           "6": "Find a Product(By SKU)",
           "7": "Receive Stock",
           "8": "Dispatch Stock",
           "9": "Create an Order",
           "10": "Add an Item to Order",
           "11": "Confirm an Order",
           "12": "Fulfil an Order",
           "13": "Cancel an Order",
           "14": "View an Order",
           "15": "Inventory Valuation",
           "16": "Low Stock Report",
           "17": "Expiry Report",
           "0": "Exit"}

actions = {"1": do_add_product,
           "2": do_add_perishable,
           "3": do_edit_product,
           "4": do_delete_product,
           "5": do_list_products,
           "6": do_find_product,
           "7": do_receive_stock,
           "8": do_dispatch_stock,
           "9": do_create_order,
           "10": do_add_to_order,
           "11": do_confirm_order,
           "12": do_fulfil_order,
           "13": do_cancel_order,
           "14": do_view_order,
           "15": do_inventory_value,
           "16": do_low_stock_report,
           "17": do_expiry_report,
        }

def start():
    choice = "1"
    while choice != "0":

        print("""<=== Welcome To The Inventory Manager ===>
Choose An Action To Perform:""")
        for key, value in labels.items():
            print(f"{key}: {value}")

        choice: str = input("Action: ")
        if choice not in labels:
            print("\n!!!!!! Enter a valid action !!!!!!\n")
            continue
        
        print(f"You Chose: {labels[choice]}")

        if choice != "0":
            actions[choice]()
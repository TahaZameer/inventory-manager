actions = {"1": "Add a Product",
           "2": "List Products",
           "0": "Exit"}

print("""<=== Welcome To The Inventory Manager ===>
Choose An Action To Perform:""")
for key, value in actions.items():
    print(f"{key}: {value}")

choice: str = input("Action: ")
print(f"You Chose: {actions[choice]}")
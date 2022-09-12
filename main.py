DATA = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2.0
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

income = 0
resources = {
    "water": 1000,
    "milk": 700,
    "coffee": 800,
}


def my_order():
    income = 0
    while True:
        order = input("What would you like? Expresso(E), Latte(L) or Cappuccino(C) or a Report(R) : ")
        if order.lower() == "report" or order.lower() == "r":
            print(f"Water : {resources['water']}")
            print(f"Milk : {resources['milk']}")
            print(f"Milk : {resources['coffee']}")
        elif order.lower() == "expresso" or order.lower() == "e":
            if resources["water"] <= 0:
                print("Water has run out!")
                break
            elif resources["milk"] <= 0:
                print("Milk has run out!")
                break
            elif resources["coffee"] <= 0:
                print("Coffee has run out!")
                break
            else:
                print("Expresso ordered")
                resources["water"] -= DATA["expresso"]["ingredients"]["water"]
                resources["coffee"] -= DATA["expresso"]["ingredients"]["coffee"]
                income += DATA["expresso"]["cost"]
        elif order.lower() == "latte" or order.lower() == "l":
            if resources["water"] <= 0:
                print("Water has run out!")
                break
            elif resources["milk"] <= 0:
                print("Milk has run out!")
                break
            elif resources["coffee"] <= 0:
                print("Coffee has run out!")
                break
            else:
                print("Latte ordered")
                resources["water"] -= DATA["latte"]["ingredients"]["water"]
                resources["milk"] -= DATA["latte"]["ingredients"]["milk"]
                resources["coffee"] -= DATA["latte"]["ingredients"]["coffee"]
                income += DATA["latte"]["cost"]
        elif order.lower() == "cappuccino" or order.lower() == "c":
            if resources["water"] <= 0:
                print("Water has run out!")
                break
            elif resources["milk"] <= 0:
                print("Milk has run out!")
                break
            elif resources["coffee"] <= 0:
                print("Coffee has run out!")
                break
            else:
                print("Cappuccino ordered")
                resources["water"] -= DATA["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= DATA["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= DATA["cappuccino"]["ingredients"]["coffee"]
                income += DATA["cappuccino"]["cost"]
        elif order.lower() == "exit":
            break
        else:
            print("Invalid option entered!")


my_order()

sec_input = input("Enter (R) to refill or (I) to check on the income : ")
if sec_input.lower() == "r" or sec_input.lower() == "refill":
    resources = {
        "water": 1000,
        "milk": 700,
        "coffee": 800,
    }
    print("\n Ingredients have been refilled \n")
    my_order()
elif sec_input.lower() == "i" or sec_input.lower() == "income":
    print(f"Income is {income}")
else:
    print("You have entered an invalid option!")


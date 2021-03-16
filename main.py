MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(order_ingredients):
    """Returns true when all the ingredients are available."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def calculate_coins():
    """ calculates inserted coins """
    print("Insert coins")
    total = int(input("How many quaters: ")) * 0.25 + int(input("how many dimes: ")) * 0.10 + int(input("how many nickels: ")) * 0.05 + int(input("how many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """ Checks if the money received is sufficient to make coffee. If not returns money"""
    global total_money
    if money_received >= drink_cost:
        refund = round(payment - drink["cost"], 2)
        total_money += drink["cost"]
        print(f"Here is ${refund} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_ingredients):
    """ Makes coffee and deduct the ingredients from resources. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy you {choice}! ☕")
    return resources[item]


total_money = 0
switch = True
while switch:
    choice = input("What would you like to have? (espresso, latte, cappuccino): ")

    if choice == "off":
        switch = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${total_money}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink["ingredients"]):
            payment = calculate_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink["ingredients"])

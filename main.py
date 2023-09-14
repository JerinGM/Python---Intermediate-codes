MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
needCoffee = True
money = 0
report = resources
while needCoffee == True:
    inputFromUser = input("What would you like? (espresso/latte/cappuccino):\n")
    if inputFromUser == 'latte' or inputFromUser == 'espresso' or inputFromUser == 'cappuccino':
        if MENU[inputFromUser]['ingredients']['water'] <= resources["water"] and MENU[inputFromUser]['ingredients']['milk'] <= resources["milk"] and MENU[inputFromUser]['ingredients']['coffee'] <= resources["coffee"]:
            print("Please insert coin")
            quarter = round(float(input("How many quarters?\n")) * 0.25, 2)
            dimes = round(float(input("How many dime?\n")) * 0.10, 2)
            nickel = round(float(input("How many nickel?\n")) * 0.05, 2)
            pennies = round(float(input("How many pennies?\n")) * 0.01, 2)
            total = quarter + dimes + nickel + pennies
            if total >= MENU[inputFromUser]['cost']:
                balance = total - MENU[inputFromUser]['cost']
                money += MENU[inputFromUser]['cost']
                print(f"Enjoy your {inputFromUser}, here is your change ${balance}")
                resources["water"] -= MENU[inputFromUser]['ingredients']['water']
                resources["coffee"] -= MENU[inputFromUser]['ingredients']['coffee']
                if inputFromUser == 'latte' or inputFromUser == 'cappuccino':
                    resources["milk"] -= MENU[inputFromUser]['ingredients']['milk']
                report = resources
            else:
                print(f"Not enough money. Here is your refund ${total}")
        else:
            print("Few ingredients to make your drink is/are missing. Regret the inconvenience caused.")
    elif inputFromUser == 'report':
        print(f"\nWater: {report['water']}ml\nMilk: {report['milk']}ml\nCoffee: {report['coffee']}g\nMoney ${money}\n")
    elif inputFromUser == 'off':
        needCoffee = False
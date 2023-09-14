from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Objects below
menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

#Varibale for while loop condition
needCoffee = True

while needCoffee is True:
    choice = input(f"What would you like to have? {menu.get_items()}")
    if choice == 'report':
        coffeemaker.report()
        moneymachine.report()
    elif choice == 'off':
        needCoffee = False
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)


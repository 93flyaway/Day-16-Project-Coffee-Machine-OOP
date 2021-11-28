from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    coffee_menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        user_drink = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()
        if user_drink == 'off':
            return
        elif user_drink == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            user_order = coffee_menu.find_drink(user_drink)
            if coffee_maker.is_resource_sufficient(user_order):
                if money_machine.make_payment(user_order.cost):
                    coffee_maker.make_coffee(user_order)


coffee_machine()

"""
Title: Coffee Machine
Author: Franco Nepomuceno
Date: 10/3/2023
Rev: A
"""

def coffee_selection(user_response, turn_off, w, c, m, dollar):
    if user_response == "report":
        print(f"Water = {w}\nMilk = {m}\nCoffee = {c}\nMoney = {dollar}\n")
        return 0  # Return a price of 0 for the report to avoid TypeError
    elif user_response == "espresso":
        return 1.50
    elif user_response == "latte":
        return 2.50
    elif user_response == "cappuccino":
        return 3.00
    elif user_input == "off":
        turn_off = False
        return 0
    else:
        print("Wrong response")
        return 0


def check_coins(user_response, q, d, n, p):
    """
    espresso = $1.50
    latte = $2.50
    cappuccino = $3.00
    """
    # Initial coin value
    total = 0

    # Add the coins
    total = round(((q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)), 2)
    # Choices and coins deposited
    if user_response == "espresso" and total >= 1.50:
        if total == 1.50:
            print("Here is your espresso. Enjoy!\nYou have '0' change")
            return total
        else:
            total = total - 1.50
            print(f"Here is your espresso. Enjoy!\nYou have ${total} change\n")
            return total
    elif user_response == "espresso" and total < 1.50:
        print(f"Not enough balance. Here is your ${total} back\n")

    elif user_response == "latte" and total >= 2.50:
        if total == 2.50:
            print(f"Here is your latte. Enjoy!\nYou have '0' change\n")
            return total
        else:
            total = total - 2.50
            print(f"Here is your latte. Enjoy!\nYou have ${total} change\n")
            return total
    elif user_response == "latte" and total < 2.50:
        print(f"Not enough balance. Here is your ${total} back")

    elif user_response == "cappuccino" and total >= 3.0:
        if total == 3.0:
            print(f"Here is your espresso. Enjoy!\nYou have '0' change\n")
            return total
        else:
            total = total - 3.0
            print(f"Here is your espresso. Enjoy!\nYou have ${total} change\n")
            return total
    elif user_response == "cappuccino" and total < 3.0:
        print(f"Not enough balance. Here is your ${total} back\n")


def check_ingredients(user_response, w, c, m):
    if user_response == "espresso":
        """
        Water = 50ml
        Coffee = 18g
        """
        if w < 50 or c < 18:
            return False, w, c, m
        else:
            w -= 50
            c -= 18
            return True, w, c, m
    elif user_response == "latte":
        """
        Water = 200ml
        Coffee = 24g
        Milk = 150ml
        """
        if w < 200 or c < 24 or m < 150:
            return True, w, c, m
        else:
            w -= 200
            c -= 24
            m -= 150
            return True, w, c, m
    elif user_response == "cappuccino":
        """
        Water = 250ml
        Coffee = 24g
        Milk = 100ml
        """
        if w < 250 or c < 24 or m < 100:
            return False, w, c, m
        else:
            w -= 250
            c -= 24
            m -= 100
            return True, w, c, m
    else:
        print("Wrong response")
        return False, w, c, m


# Initial variables

Water = 5000 # Default is 300mk
Milk = 1000 # Default is 200ml
Coffee = 1000 # Default is 100g
Money = 0

machine_status = True
while machine_status:
    print("Welcome to Franco's Coffee Shop")
    user_input = input("What would you like to order? (espresso/latte/cappuccino):\t").lower()
    #  print(f"Water {Water}, Milk {Milk}, Coffee {Coffee}")

    if user_input == "off":
        machine_status = False
    elif user_input == "report":
        coffee_selection(user_input, machine_status, Water, Coffee, Milk, Money)  # Just print the report
    else:
        # price = price of coffee
        price = coffee_selection(user_input, machine_status, Water, Coffee, Milk, Money)
        print(f"A cup of {user_input} cost ${coffee_selection(user_input, machine_status, Water, Coffee, Milk, Money)}\n")
        if price > 0:
            success, Water, Coffee, Milk = check_ingredients(user_input, Water, Coffee, Milk)
            if success:
                print("Please insert coins")
                quarters = int(input("How many quarters?:\t"))
                dimes = int(input("How many dimes?:\t"))
                nickels = int(input("How many nickels?:\t"))
                pennies = int(input("How many pennies?:\t"))
                total_change = check_coins(user_input, quarters, dimes, nickels, pennies)
                # print(f"Test Total Change: {check_coins(user_input, quarters, dimes, nickels, pennies)}\n")
                total_coins = round(((quarters * 0.25) + (dimes * .10) + (nickels * 0.05) + (pennies * 0.01)), 2)

                if  total_coins >= price:
                    Money += price
                    print(f"Here is your {user_input}. Enjoy!\n")
                else:
                    print(f"Not enough balance. Here is your ${total_coins} back\n")
            else:
                print(f"Sorry, not enough ingredients for {user_input}\n")





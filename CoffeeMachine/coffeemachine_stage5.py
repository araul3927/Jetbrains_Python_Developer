water, milk, coffee, money, cups = 400, 540, 120, 550, 9

def show_inventory():
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee} of coffee beans
{cups} of disposable cups
{money} of money\n""")

def coffee_making(waterneeded = 0, milkneeded = 0, coffeeneeded = 0, moneyneeded = 0):
    global water, milk, coffee, cups, money
    if water - waterneeded < 0:
        print("Sorry, not enough water!")
    elif coffee - coffeeneeded < 0:
        print("Sorry, not enough coffee!")
    elif milk - milkneeded < 0:
        print("Sorry, not enough milk!")
    elif cups - 1 < 0:
        print("Sorry, not enough cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water -= waterneeded
        milk -= milkneeded
        coffee -= coffeeneeded
        money += moneyneeded
        cups -= 1

def buy_coffee():
    global water, milk, coffee, cups, money
    order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if order == "1":
        coffee_making(250, 0, 16, 4)
    elif order == "2":
        coffee_making(350, 75, 20, 7)
    elif order == "3":
        coffee_making(200, 100, 12, 6)

def fill_machine():
    global water, milk, coffee, cups
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    coffee += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
    
def take_money():
    global money
    print(f"I gave you ${money}")
    money = 0

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "buy":
        buy_coffee()
    elif action == "fill":
        fill_machine()
    elif action == "take":
        take_money()
    elif action == "remaining":
        show_inventory()
    elif action == "exit":
        break
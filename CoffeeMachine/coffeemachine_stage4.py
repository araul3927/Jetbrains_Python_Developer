money = 550
water = 400
milk = 540
coffee_beans = 120
dis_cups = 9


def accounting():
    print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{dis_cups} of disposable cups
{money} of money
""")


def buy():
    command_buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
    global money, water, milk, coffee_beans, dis_cups
    if command_buy == '1':
        water -= 250
        coffee_beans -= 16
        money += 4
        dis_cups -= 1
    elif command_buy == '2':
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
        dis_cups -= 1
    elif command_buy == '3':
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
        dis_cups -= 1


def fill():
    global water, milk, coffee_beans, dis_cups
    water += int(input('Write how many ml of water do you want to add:'))
    milk += int(input('Write how many ml of milk do you want to add:'))
    coffee_beans += int(input('Write how many grams of coffee beans do you want to add:'))
    dis_cups += int(input('Write how many disposable cups of coffee do you want to add:'))

def take():
    global money
    print(f'I gave you ${money}')
    money -= money


accounting()
command = input('Write action (buy, fill, take):')
if command == 'buy':
    buy()
elif command == 'fill':
    fill()
elif command == 'take':
    take()
accounting()
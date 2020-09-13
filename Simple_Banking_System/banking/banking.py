
import random
import sqlite3

Accounts = {}

class Card:
    def __init__(self):
        self.iin = '400000'
        self.pin = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        self.number = None
        self.checksum = None
        self.customer_account = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        self.partial_number = self.iin + self.customer_account
        self.generate_number()

    def generate_number(self):
        numbers = [int(x) for x in self.partial_number]
        for idx, num in enumerate(numbers):
            if idx % 2 == 0:
                num *= 2
            if num > 9:
                num -= 9
            numbers[idx] = num
        self.checksum = str((10 - sum(numbers) % 10) % 10)
        self.number = self.partial_number + self.checksum

class Account:
    number_accounts = 0
    def __init__(self):
        self.balance = 0
        self.card = Card()
        self.id = Account.number_accounts + 1
        Account.number_accounts += 1


    def card_pin(self):
        return self.card.pin

    def card_number(self):
        return self.card.number

def add_account(account):
    Accounts[account.card_number()] = {'pin': account.card_pin(), 'balance': account.balance}

def verify_card_number(number):
    numbers = [int(x) for x in number]
    last_number = numbers.pop()
    for idx, num in enumerate(numbers):
        if idx % 2 == 0:
            num *= 2
        if num > 9:
            num -= 9
        numbers[idx] = num
    numbers.append(last_number)
    return sum(numbers) % 10 == 0
def menu1():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    choice = input()
    return choice

def menu2():
    print('1. Balance')
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
    print('0. Exit')
    choice = input()
    return choice

def generate_account():
    account = Account()
    add_account(account)
    print('Your card has been created')
    print('Your card number:')
    print(account.card_number())
    print('Your card PIN:')
    print(account.card_pin())
    add_database(account)

def log_in():
    print('Enter your card number:')
    number = input()
    print('Enter your PIN:')
    pin = input()
    print()
    if number not in Accounts:
        print('Wrong card number or PIN!')
    elif Accounts[number]['pin'] != pin:
        print('Wrong card number of PIN!')
    else:
        print('You have successfully logged in!')
        return True, number
    return False, None

def get_balance(card_number):
    print('Balance:', check_balance(card_number))

def create_database():
    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS card (
    id INTEGER, 
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
    );''')

    conn.commit()
    conn.close()

def add_database(account):
    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO card VALUES(?, ?, ?, ?);', (account.id, account.card_number(), account.card_pin(), 0))
    conn.commit()
    conn.close()

def check_balance(card_number):
    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM card WHERE number = ?;', (card_number,))
    balance = cursor.fetchone()
    conn. commit()
    conn.close()
    return balance

def add_income(card_number):
    print('Enter income:')
    income = int(input())
    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()
    cursor.execute('UPDATE card SET balance = balance + ? WHERE number = ?;', (income, card_number))
    conn.commit()
    conn.close()

def do_transfer(card_number):
    print('Transfer')
    print('Enter card number:')
    number = input()
    if not verify_card_number(number):
        print('Probably you made mistake in the card number. Please try again!')
        return
    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()
    if check_balance(number) is None:
        print('Such a card does not exist.')
        return
    print('Enter how much money you want to transfer:')
    transfer = int(input())
    if check_balance(card_number)[0] >= transfer:
        conn = sqlite3.connect('card.s3db')
        cursor = conn.cursor()
        cursor.execute('UPDATE card SET balance = balance + ? WHERE number = ?;', (transfer, number))
        cursor.execute('UPDATE card SET balance = balance - ? WHERE number = ?;', (transfer, card_number))
        conn.commit()
        conn.close()
    else:
        print('Not enough money!')

def close_account(card_number):
    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM card WHERE number = ?', (card_number,))
    conn.commit()
    conn.close()


def main():
    create_database()
    choice = menu1()
    print()
    while choice != '0':
        if choice == '1':
            generate_account()
        elif choice == '2':
            possible, card_number = log_in()
            if possible:
                choice2 = menu2()
                print()
                while choice2 != '0':
                    if choice2 == '1':
                        get_balance(card_number)
                    elif choice2 == '2':
                        add_income(card_number)
                    elif choice2 == '3':
                        do_transfer(card_number)
                    elif choice2 == '4':
                        close_account(card_number)
                    elif choice2 == '5':
                        print('You have successfully logged out!')
                        break
                    choice2 = menu2()
                if choice2 == '0':
                    print('Bye!')
                    return
        else:
            print('Bye!')
            return
        choice = menu1()
        print()

main()
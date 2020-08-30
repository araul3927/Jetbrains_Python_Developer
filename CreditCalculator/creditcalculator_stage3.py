from math import ceil, log
def format_months(months):
    years_str = months_str = separator = ''
    years = months // 12
    months = months % 12
    if years != 0:
        years_str += f'{years} year'
        if years != 1:
            years_str += 's'
    if months != 0:
        months_str += f'{months} month'
        if months != 1:
            months_str += 's'
    if not(months == 0 or years == 0):
        separator += ' and '

    return years_str + separator + months_str

print('''What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal:''')
choice = input()

if choice == 'n':
    print('Enter credit principal:')
    principal = float(input())
    print('Enter monthly payment:')
    monthly_payment = float(input())
    print('Enter credit interest:')
    interest = float(input()) / 1200

    months = ceil(log(monthly_payment / (monthly_payment - interest * principal), 1 + interest))
    print(f' You need {format_months(months)} to repay this credit!')
elif choice == 'a':
    print('Enter credit principal:')
    principal = float(input())
    print('Enter count of periods:')
    months = int(input())
    print('Enter credit interest:')
    interest = float(input()) / 1200

    annuity = principal * (interest * pow(1 + interest, months) / (pow(1 + interest, months) - 1))
    print(f'Your annuity payment = {ceil(annuity)}!')
else:
    print('Enter monthly payment:')
    monthly_payment = float(input())
    print('Enter count of periods:')
    months = int(input())
    print('Enter credit interest:')
    interest = float(input()) / 1200

    principal = monthly_payment / (interest * pow(1 + interest, months) / (pow(1 + interest, months) - 1))
    print(f'Your credit principal = {ceil(principal)}!')
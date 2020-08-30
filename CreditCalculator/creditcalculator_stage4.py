import argparse
import sys
import math
parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, help='It indicates the type of payment: "annuity" or "diff"')
parser.add_argument("--periods", type=float, help="takes the count of months")
parser.add_argument("--principal", type=float, help="takes the amount borrowed or amount to be borrowed")
parser.add_argument("--interest", type=float, help="takes the interest charged without the percentage symbol")
parser.add_argument("--payment", type=float, help="takes the monthly payment amount")

args = parser.parse_args()
types = args.type
periods = args.periods
interest = args.interest
month_pay = args.payment
principal = args.principal

if types not in ["annuity", "diff"]:
    print("Incorrect parameters")
    sys.exit()
elif len(sys.argv) != 5:
    print("Incorrect parameters")
    sys.exit()
elif types is None:
    print("Incorrect parameters")
    sys.exit
elif periods is not None and periods != abs(periods):
    print("Incorrect parameters")
    sys.exit()
elif month_pay is not None and month_pay != abs(month_pay):
    print("Incorrect parameters")
    sys.exit()
elif principal is not None and principal != abs(principal):
    print("Incorrect parameters")
    sys.exit()
elif interest is not None and interest != abs(interest):
    print("Incorrect parameters")
    sys.exit()
elif types == "diff" and month_pay is not None:
    if principal is None or periods is None:
        print("Incorrect parameters")
        sys.exit()
elif types == "diff" and month_pay is None:
    i = interest / (12 * 100)
    m = 0
    total = 0
    while m < periods:
        m += 1
        diff_pay = (principal / periods) + (i * (principal - ((principal * (m - 1)) / periods)))
        total += math.ceil(diff_pay)
        print(f"Month {m}: paid out {math.ceil(diff_pay)}")
    print(f"\nOverpayment = {int(total - principal)}")
    sys.exit()
elif types == "annuity" and month_pay is None:
    i = interest / (12 * 100)
    month_pay = principal * ((i * ((1 + i)**periods)) / (((1 + i)**periods) - 1))
    anuit_pay = math.ceil(month_pay)
    overpayment = (anuit_pay * periods) - principal
    print(f"Your annuity payment = {anuit_pay}!")
    print(f"Overpayment = {int(overpayment)}")
    sys.exit()
elif types == "annuity" and principal is None:
    i = interest / (12 * 100)
    principal = month_pay / ((i * ((1 + i)**periods)) / (((1 + i)**periods) - 1))
    p = math.floor(principal)
    over_p = (month_pay * periods) - p
    print(f"Your credit principal = {p}!")
    print(f"Overpayment = {int(over_p)}")
    sys.exit()
elif types == "annuity" and periods is None:
    i = interest / (12 * 100)
    periods = (math.log(month_pay / (month_pay - (i * principal)))) / (math.log(1 + i))
    year = math.ceil(periods / 12)
    over_p = (year * 12 * month_pay) - principal
    if year > 1:
        print(f"You need {year} years to repay this credit!")
    elif year == 1 or year == 0:
        print(f"You need {year} year to repay this credit!")
    print(f"Overpayment = {int(over_p)}")
    sys.exit()
else:
    print("Incorrect parameters")
    sys.exit()
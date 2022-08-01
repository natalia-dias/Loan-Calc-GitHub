import math
import argparse


def ann_payment(principal, periods, interest):
    int_rate = float(interest / 100 / 12)
    payment = math.ceil(principal * ((int_rate * ((1 + int_rate) ** periods)) /     # might be an error with math,floor
                        ((1 + int_rate) ** periods - 1)))
    print(f'Your annuity payment = {payment}!')
    print("Overpayment = ", int(payment * periods - principal))


def time(principal, payment, interest):
    int_rate = float(interest / 100 / 12)
    x = payment / (payment - int_rate * principal)
    months = math.log(x, 1 + int_rate)
    total_months = math.ceil(months)

    if 12 > total_months > 1:
        print(f'It will take {total_months} months to repay this loan!')
    if total_months == 1:
        print('It will take 1 month to repay this loan!')
    if total_months == 12:
        print('It will take 1 year to repay this loan!')
    else:
        y = math.floor(total_months / 12)
        m = total_months % 12
        if y == 1 and m == 1:
            print('It will take 1 year and 1 month to repay this loan!')
        if y == 1 and m > 1:
            print(f'It will take 1 year and {m} months to repay this loan!')
        if y > 1 and m == 0:
            print(f'It will take {y} years to repay this loan!')
        if y > 1 and m == 1:
            print(f'It will take {y} years and 1 month to repay this loan!')
        if y > 1 and m > 1:
            print(f'It will take {y} years and {m} months to repay this loan!')
    print("Overpayment = ", int(payment * total_months - principal))


def diff_payments(principal, periods, interest):
    if principal < 0 or periods < 0 or interest < 0:
        print('Incorrect parameters.')
    else:
        int_rate = float(interest / 100 / 12)
        m = 1
        over = 0
        while m <= periods:
            d = math.ceil((principal / periods) + int_rate * (principal - (principal * (m - 1)/periods)))
            print(f'Month {m}: payment is {d}')
            m += 1
            over += d
        print("Overpayment = ", int(over - principal))


def principal(payment, periods, interest):
    int_rate = float(interest / 100 / 12)
    principal = math.floor(payment / (int_rate * ((1 + int_rate) ** periods) / (((1 + int_rate) ** periods) - 1)))
    print(f'Your loan principal = {principal}!')
    print("Overpayment = ", int(payment * periods - principal))


parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument('-t', '--type', type=str)
parser.add_argument('-pr', '--principal', type=int)
parser.add_argument('-in', '--interest', type=float)
parser.add_argument('-p', '--periods', type=int)
parser.add_argument('-pay', '--payments', type=int)
args = parser.parse_args()

if args.type is None:
    print('Incorrect parameters.')
if args.type == "diff" and args.payments is None:
    print('Incorrect parameters.')
if args.type == 'annuity' and args.principal is not None and args.periods is not None and args.interest is not None:
    ann_payment(args.principal, args.periods, args.interest)
if args.type == 'diff' and args.principal is not None and args.periods is not None and args.interest is not None:
    diff_payments(args.principal, args.periods, args.interest)
if args.type == 'annuity' and args.principal is not None and args.payments is not None and args.interest is not None:
    time(args.principal, args.payments, args.interest)
if args.type == 'annuity' and args.payments is not None and args.periods is not None and args.interest is not None:
    principal(args.payments, args.periods, args.interest)

# write your code here
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['annuity', 'diff'], help="Different pay type")
# parser.add_argument('--type', choices=['annuity', 'diff'], required=True, help="Different pay type")
parser.add_argument('--principal', help="the loan principal")
parser.add_argument('--payment', help="the payment month")
parser.add_argument('--periods', help="number of payments")
parser.add_argument('--interest',  help="nominal interest rate")
# parser.add_argument('--interest', required=True, help="nominal interest rate")
args = parser.parse_args()

loan_type = args.type
if args.principal:
    principal = float(args.principal)
else:
    principal = None
if args.payment:
    payment = float(args.payment)
if args.periods:
    periods = int(args.periods)
else:
    periods = None
if args.interest:
    interest = float(args.interest)
else:
    interest = None



def cal_interest(input_interest):
    return (input_interest * 0.01) / 12


def cal_diff_payment(input_principal, input_periods, input_interest, input_month):
    return input_principal / input_periods + \
           input_interest * (input_principal - (input_principal * (input_month - 1) / input_periods))


def cal_ann_payment(input_principal, input_periods, input_interest):
    return input_principal * \
           ((input_interest * (1 + input_interest) ** input_periods) / ((1 + input_interest) ** input_periods - 1))

def cal_principal(input_payment, input_periods, input_interest):
    return input_payment / \
           ((input_interest * (1 + input_interest) ** input_periods) / ((1 + input_interest) ** input_periods - 1))

if loan_type == "diff" and principal is not None and periods is not None and interest is not None:
    input_interest = cal_interest(interest)
    sum = 0
    for i in range(periods):
        month_payment = math.ceil(cal_diff_payment(principal, periods, input_interest, i+1))
        sum += month_payment
        print("Month {}: payment is {}".format(i+1, month_payment))
    print("")
    print("Overpayment = {}".format(int(sum - principal)))

elif loan_type == "annuity" and principal is not None and periods is not None and interest is not None:
    input_interest = cal_interest(interest)
    ann_payment = math.ceil(cal_ann_payment(principal, periods, input_interest))
    print("Your annuity payment = {}!".format(ann_payment))
    print("Overpayment = {}".format(int(ann_payment * periods - principal)))
elif loan_type == "annuity" and payment is not None and periods is not None and interest is not None:
    input_interest = cal_interest(interest)
    loan_principal = math.floor(cal_principal(payment, periods, input_interest))
    print("Your loan principal = {}!".format(loan_principal))
    print("Overpayment = {}".format(int(payment * periods - loan_principal)))
elif loan_type == "annuity" and principal is not None and payment is not None and interest is not None:
    input_interest = cal_interest(interest)
    base = payment / (payment - input_interest * principal)
    total_month = math.ceil(math.log(base, 1 + input_interest))
    if total_month < 12:
        print("It will take {} months to repay this loan!".format(total_month))
        print("Overpayment = {}".format(int(payment * total_month - principal)))
    else:
        if total_month % 12 == 0:
            print("It will take {} years to repay this loan!".format(total_month // 12))
            print("Overpayment = {}".format(int(payment * total_month - principal)))
        else:
            pay_year = total_month // 12
            pay_month = total_month % 12
            print("It will take {} years and {} months to repay this loan!".format(pay_year, pay_month))
            print("Overpayment = {}".format(int(payment * total_month - principal)))
else:
    print("Incorrect parameters")

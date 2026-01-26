BASE_HOURS = 40
OT_MULTIPLIER = 1.5

hours = float(input("enter the number of hours worked: "))
pay_rate = float(input("enter the hourly pay rate: "))

if hours > 40:
    overtime_hours = hours - BASE_HOURS

    overtime_pay = overtime_hours * OT_MULTIPLIER * pay_rate

    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    gross_pay = hours * pay_rate

print(f"The gross pay is ${gross_pay:,.2f}.")

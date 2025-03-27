# Shaun Beard
# 3/27/2025
# P4HW2
# program will calculate gross pay for multiple employees with same orginal program

# Input
employee_name = input("Enter employee's name or 'Done' to Terminate: ")
counter = 0
total_Ot = float()
total_Reg = float()
total_gross = float()

while employee_name != "Done":

    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    if hours_worked > 40:
        OT_hours = float(hours_worked - 40)
        OT_payrate = float(pay_rate * 1.5)
        OT_pay = float(OT_hours * OT_payrate)
        Reg_pay = float(40 * pay_rate)
        gross_pay = float(OT_pay + Reg_pay)
    else: 
        OT_hours = 0
        OT_payrate = 0
        OT_pay = 0
        Reg_pay = float(hours_worked * pay_rate)
        gross_pay = (Reg_pay)

    total_Ot = total_Ot + OT_pay
    total_Reg = total_Reg + Reg_pay
    total_gross = total_gross + gross_pay
    print("-----------" * 3)
    print(f"Employee name:  {employee_name}")
    print()
    print(f"{'Hours Worked':<20}${'Pay Rate':<20}{'OverTime':<20}${'OverTime Pay':<20}${'RegHour Pay':<20}${'Gross Pay':<20}")
    print("-----------" * 8)
    print(f"{hours_worked:<20.1f}${pay_rate:<20.2f}{OT_hours:<20.1f}${OT_pay:<20.2f}${Reg_pay:<20.2f}${gross_pay:<20.2f}")
    print()
    print()
    counter += 1
    employee_name = input("Enter employee's name or 'Done' to Terminate: ")

print()
print(f"Total number of employees Entered: {counter}")
print(f"Total amount paid for overtime: {total_Ot}")
print(f"Total amount paid for regular hours: {total_Reg}")
print(f"Total amount paid in gross: {total_gross}")



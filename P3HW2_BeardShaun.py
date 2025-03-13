# Shaun Beard
# 3/13/2025
# P3HW2
# Determine OT pay, regular pay, and gross pay

''' 
Pseudocode:

Get employee_name from user (variable needed and use input)
Get hours_worked from user ( float variable and use input)
Get pay_rate from user (float variable and use input)

determine if the employee worked OT

if hours_worked > 40 
    Calculate OT_hours (hours_worked - 40) (Overtime_hours variable)
    Calculate OT_payrate (pay_rate * 1.5) (OT_payrate variable)
    Calculate OT_pay (OT_hours * OT_payrate) (OT_pay variable)
    Calculate Reg_pay (40 * pay_rate) (Reg_pay variable)
    Calculate gross_pay (OT_pay + Reg_pay)

# When hours worked are less than or equal to 40
else: 
    Calculate OT_hours = 0
    Calculate OT_payrate = 0 
    Calculate Reg_pay (hours_worked + pay_rate)
    Calculate gross_pay (OT_pay + Reg_pay)

Output the values
display the employee name separately
display all heading (formatted)
display doted line
display the values of the headings (formatted)


hours_worked = 35
pay_rate = 6.00

# display the values in columes
print(f"{'Hours Worked':<20}{'Pay Rate':<20}")
print("-----------" * 5)
print(f"{hours_worked:<20}${pay_rate:<20.2f}")
'''

# Python


# Input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculatons
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

# Output
print("-----------" * 3)
print(f"Employee name:  {employee_name}")
print()
print(f"{'Hours Worked':<20}${'Pay Rate':<20}{'OverTime':<20}${'OverTime Pay':<20}${'RegHour Pay':<20}${'Gross Pay':<20}")
print("-----------" * 8)
print(f"{hours_worked:<20.1f}${pay_rate:<20.2f}{OT_hours:<20.1f}${OT_pay:<20.2f}${Reg_pay:<20.2f}${gross_pay:<20.2f}")

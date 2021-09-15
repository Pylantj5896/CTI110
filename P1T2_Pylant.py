#CTI 110
#P1T2 -salary calculator
#Jacob Pylant
#9/15/2021

# Start
hoursWorked = input("how many hours did you work this week? ")
hoursWorked = float(hoursWorked)

# Input hours worked
hourlyPay = float(input("whats your hourly pay rate? "))

# Input hourly pay rate
grossPay = hoursWorked * hourlyPay

# Calculate gross pay (hours worked times pay rate)
print("Your gross pay for the week is: $", grossPay)
# End
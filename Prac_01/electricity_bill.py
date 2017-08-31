TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

user_tariff = int(input(" Which tariff? 11 or 31: "))
daily_use = float(input("enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

if user_tariff == 11:
    userT_tariff = TARIFF_11
elif user_tariff == 31:
    user_tariff =  TARIFF_31

estimate = (user_tariff / 100) * daily_use * billing_days
print("$",estimate)
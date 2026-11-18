year = int(input("Enter year: "))

print("\n" + "=" * 40)
print("       CALENDAR VERIFICATION SYSTEM")
print("=" * 40)

if year <= 0:
    print("Error: Please enter a positive year.")
else:
    if year % 400 == 0:
        status = "LEAP YEAR"
        reason = "Century year divisible by 400"
        days = 366
        feb_days = 29

    elif year % 100 == 0:
        status = "COMMON YEAR"
        reason = "Century year not divisible by 400"
        days = 365
        feb_days = 28

    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 4 and not a century year"
        days = 366
        feb_days = 29

    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"
        days = 365
        feb_days = 28

    print("-" * 40)
    print("Year:", year)
    print("Status:", status)
    print("Days in Year:", days, "days")
    print("Days in February:", feb_days, "days")
    print("Reason:", reason)
    print("-" * 40)
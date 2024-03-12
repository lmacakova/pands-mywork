percentage = float(input("Enter the percentage: "))
if percentage < 0 or percentage > 100:
    print("Please enter the number between 0 and 100 (included)")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 1")
elif percentage < 70:
    print("Merit 2")
elif percentage < 80:
    print("Distinctive")
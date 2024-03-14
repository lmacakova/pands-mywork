percentage = float(input("Enter the percentage: "))
roundedPercentage = round(percentage)
if roundedPercentage < 0 or roundedPercentage > 100:
    print("Please enter the number between 0 and 100 (included)")
elif roundedPercentage < 40:
    print("Fail")
elif roundedPercentage < 50:
    print("Pass")
elif roundedPercentage < 60:
    print("Merit 1")
elif roundedPercentage < 70:
    print("Merit 2")
elif roundedPercentage < 80:
    print("Distinctive")
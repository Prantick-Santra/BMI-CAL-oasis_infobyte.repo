weight=float(input("Enter your weight in pounds: "))
height=float(input("Enter your height in inches: "))
BMI=((weight)/(height**2))*703
print(f"Your BMI is: {BMI}")
print("According to BMI, you are:")
if(BMI<=16):
    print("Severe Thinness")
elif(16<BMI<=17):
    print("Moderate Thinness")
elif(17<BMI<=18.5):
    print("Mild Thinness")
elif(18.5<BMI<=25):
    print("Normal")
elif(25<BMI<=30):
    print("Overweight")
elif(30<BMI<=35):
    print("Obese Class I")
elif(35<BMI<=40):
    print("Obese Class II")
else:
    print("Obese Class III")
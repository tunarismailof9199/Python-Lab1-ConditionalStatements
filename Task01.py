weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
BMI = weight / (height*height)
print("BMI = ", BMI)
if BMI < 18.5:
    print("Category: Underweight")
elif 18.5<=BMI<=24.9:
    print("Category: Normal Weight")
elif 25.0<=BMI<=29.9:
    print("Category: Overeight")
elif 30<=BMI:
    print("Category: Obese")
    

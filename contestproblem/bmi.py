#need height and weight input
#display 
#overloaded methods are methods with the same name but are distinguished 
#based on their parameters


weight = input("Enter weight:")
height = input()
weight = float(weight)
height = float(height)

BMI = weight/(height * height)

if (BMI > 25.0):
    print ("Overweight")

elif (18.5 <= BMI <= 25.0):
    print ("Normal weight")

elif (BMI < 18.5):
    print ("Underweight")
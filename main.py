
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")



int_height = float(height)
int_weight = float(weight)

BMI = (int_weight / (int_height * int_height))
a = "Underweight"
b = "Normal Weight"
c = "Overweight"
d = "Obese"
float(BMI)
print(BMI)
if (BMI < 18.5):
        print("You are " + a)
if (BMI > 18.5 and BMI < 24.9):
        print("You are " + b)
if (BMI > 25 and BMI < 29.9):
        print("You are " + c)
if (BMI > 30):
        print("You are " + d)







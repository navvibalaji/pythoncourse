#input from user
height = float(input("enter height()cm: "))
weight = float(input("enter weight()kg: "))

#bmi calculation
bmi=weight/ (height/100)**2
print(bmi)
if(bmi<=18.4):
    print("the person is underweight")
elif(bmi>=25.2):
    print("the person is overweight")
elif(bmi>=18.4 and bmi<=25.2):
    print("the person is healthy")
else:
    print("the person is obese")

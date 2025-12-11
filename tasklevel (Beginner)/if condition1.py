'''1. Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"'''

'''2. Write a program to determine which country a city belongs to. Given
list of cities per country:
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
Ask the user to enter a city name and print the corresponding country.'''

'''3. Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the
same country or not.'''
#1
print("enter height in meter") 
height=float(input())
print("enter weight in kilograms")
weight=float(input())
bmi=weight/(height **2)
print("BMI is ",bmi)
if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("overweight")
elif 18.5 <= bmi <25:
    print("normal")
else:
    print("underweight")
#2
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city=input("enter the city name:")
if city in Australia:
    print(f"{city} is in Australia")

elif city in UAE:
    print(f"{city} is in UAE")

elif city in India:
    print(f"{city} is in India")

else:
    print("City not found in any list")
#3
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city1=input("enter a city:")
city2=input("enter another city:")
if city1 in Australia and city2 in Australia:
    print(f"{city1} and {city2} belongs to same country")
elif city1 in UAE and city2 in UAE:
        print(f"{city1} and {city2} belongs to same country")
elif city1 in India and city2 in India:
            print(f"{city1} and {city2} belongs to same country")
else:
     print("both cities are not present in the same country")





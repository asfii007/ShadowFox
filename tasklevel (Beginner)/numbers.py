'''1. Write a function that takes two arguments, 145 and 'o'
,and uses the format` function to return a formatted string. Print the
result. Try to identify the representation used.'''
'''2. In a village, there is a circular pond with a radius of 84 meters.
Calculate the area of the pond using the formula: Circle Area = π
r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
1.4 liters of water in a square meter, what is the total amount of
water in the pond? Print the answer without any decimal point in
it. '''
'''3. If you cross a 490meterlong street in 7 minutes, calculate your
speed in meters per second. Print the answer without any decimal
point in it. Hint: Speed = Distance / Time'''
#1
def format_value(number, fmt):
    return format(number, fmt)

result = format_value(145, 'o')
print(result)
#2
pi = 3.14
r = 84

area = pi * (r ** 2)
water = int(area * 1.4)   # removes decimal point

print("Area of pond:", area)
print("Total water in liters:", water)
#3
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60

speed = int(distance / time_seconds)   # no decimal
print("Speed (m/s):", speed)

'''1. Create a variable named pi and store the value 22/7 in it.
Now check the data type of this variable.'''

'''2. Create a variable called for and assign it a value 4. See what
happens and find out the reason behind the behavior that you
see.'''

'''3. Store the principal amount, rate of interest, and time in
different variables and then calculate the Simple Interest for 3
years. Formula: Simple Interest = P x R x T / 100'''
#1
pi=22/7
print(pi)
print(type(pi))
#2 
#for cannot be used as a variable name because it is a keyword.
#3
P=30000
R=6
T=3
simple_interest=P*R*T/100
print(simple_interest)
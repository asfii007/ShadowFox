'''1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row'''
'''2. Imagine you are doing a workout routine, and you have to complete 100
jumping jacks.
Write a program that:
Asks you to perform 10 jumping jacks at a time.
After each set, it asks, "Are you tired?"'''
#1
import random
a=0
b=0
c=0
previous_roll=0
for i in range(20):
    roll=random.randint(1,6)
    print(roll)
    if roll==6:
        a=a+1
    if roll==1:
        b+=1
    if previous_roll ==6 and roll==6:
        c+=1
    previous_roll=roll
print(f"Total 6s rolled: {a}")
print(f"Total 1s rolled: {b}")
print(f"Number of times two 6s appeared in a row: {c}")
#2
import time
print('ready for workout!,goal is to complete 100 jumping jacks')
for i in range(1,101):
    print(i)
    time.sleep(1)
    if i%10==0 and i<100:
        print("You have completed", i, "jumping jacks.")
        print("are you tired?(Y/N)")
        reply=input().upper()
        if reply=="Y":
            print("Great job! You completed", i, "jumping jacks. Take rest.")
            break
        else :
            print("Keep going! Next set starting...\n")
            continue
if i == 100:
    print(" Congratulations! You finished all 100 jumping jacks!")
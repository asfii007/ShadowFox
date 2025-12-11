'''1. Create a list of your friends' names. The list should have at least 5 names.
Create a list of tuples. Each tuple should contain a friend's name and the length
of the name.
For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)'''

''' 2.You and your partner are planning a trip, and you want to track expenses.
Create two dictionaries, one for your expenses and one for your partner's
expenses. Each dictionary should contain at least 5 expense categories and their
corresponding amounts.'''
''' Calculate the total expenses for each of you and print the results.
Determine who spent more money overall and print the result.
Find out the expense category where there is a significant difference in spending
between you and your partner.
Print the category and the difference.'''
#1
names=["asfiya","hena","afifa","naziya","japya","apoorva"]
friend=[("asfiya",6),("hena",4),("afifa",5),("naziya",6),("japya",5),("apoorva",7)]
print(friend)

#2
men={
    "flight_ticket":12000,
    "local_transport":800,
    "food and drinks":1200,
    "clothing":900,
    "items":300
}
women={
    "flight_ticket":12000,
    "local_transport":800,
    "food and drinks":1100,
    "clothing":1200,
    "items":900
}
total=sum(men.values())
print(f"total expense of men is {total}")
total1=sum(women.values())
print(f"total expense of women is {total1}")

if total>total1:
    print(f"men expense is higher that is {total}")
elif total1>total:
    print(f"women expense is higher that is {total1}")
else:
    print("both expenses are same ")

max_diff = 0
biggest_category = None
for category in men:
    diff = abs(men[category] - women[category])
    if diff > max_diff:
        max_diff = diff
        biggest_category = category

print(f"The biggest difference is in '{biggest_category}' with a difference of {max_diff}.")

    
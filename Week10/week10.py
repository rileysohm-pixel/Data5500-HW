#1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

table = []

for i in range(1, num1 + 1):
    table.append([])
    for j in range(1, num2 + 1):
        table[i - 1].append(i * j)

for row in table:
    for value in row:
        print(value, end="\t")
    print()

#2
me = {}
me["Age"] = int(input("What is your age: "))
me["favorite_color"] = input("What is your favorite color: ")
me["multiplication_table"] = table

for key in me.keys():
    print(key,":", me[key])

#3

# import json

# with open("person.json") as file:
#     person = json.load(file)

# print(person["age"])
# person["age"] += 1
# print(person["age"])

# with open("person.json", "w") as file:
# 	json.dump(person, file, indent=4)

#4

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

try:
    num1 / num2
except:
     print("Error, attempted to divide by zero")
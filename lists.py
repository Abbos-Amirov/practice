'''
(2) List methods
(3) Lambda function
(4) enumerate, map and filter
'''

print("===== Working with lists =====")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list

for team in groups:
    print(f"the team: {team}")


# constructor
letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")


print("------")

fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # [0, 2)
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("===== List methods =====")


print("===== Lambda function =====")

# lambda is small anonymous function!


def calculate(x, y):
    return x * y


result = calculate(3, 5)

print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]

people.sort()
print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])

print("people(2)", people)

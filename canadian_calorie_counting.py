burger = int(input())
drink = int(input())
sideOrder = int(input())
dessert = int(input())

calories = 0

if burger == 1:
    calories = calories + 461
elif burger == 2:
    calories = calories + 431
elif burger == 3:
    calories = calories + 420


if drink == 1:
    calories = calories + 130
elif drink == 2:
    calories = calories + 160
elif drink == 3:
    calories = calories + 118

if sideOrder == 1:
    calories = calories + 100
elif sideOrder == 2:
    calories = calories + 57
elif sideOrder == 3:
    calories = calories + 70

if dessert == 1:
    calories = calories + 167
elif dessert == 2:
    calories = calories + 266
elif dessert == 3:
    calories = calories + 75

print(f"Your total Calorie count is {calories}.")
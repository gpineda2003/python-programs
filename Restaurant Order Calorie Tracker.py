from math import *
from time import *

Menu1 = [["Cheeseburger",461], ["Fish Burger",431], ["Veggie Burger",420], ["No Burger",0]]
Menu2 = [["Soft Drink", 130], ["Orange Juice", 160], ["Milk", 118], ["No Drink", 0]]
Menu3 = [["Fries", 100], ["Baked Potato", 57], ["Chef Salad", 70], ["No Side Order", 0]]
Menu4 = [["Apple Pie", 167], ["Sundae", 266], ["Fruit Cup", 75], ["No Desert", 0]]

print("Welcome to Gian's Restaurant!\n")

print("Here is our burger menu:")

for i in range(4):
    print((str(i + 1)) + ".", " " + (str(Menu1[i][0])), "(Calories:", (str(Menu1[i][1])) + ")")

choice1 = int(input("\nType the number corresponding to the burger you would like to select.\n")) - 1

print("\nHere is our drink menu:")

for i in range(4):
    print((str(i + 1)) + ".", " " + (str(Menu2[i][0])), "(Calories:", (str(Menu2[i][1])) + ")")

choice2 = int(input("\nType the number corresponding to the drink you would like to select.\n")) - 1
            
print("\nHere is our side menu:")

for i in range(4):
    print((str(i + 1)) + ".", " " + (str(Menu3[i][0])), "(Calories:", (str(Menu3[i][1])) + ")")

choice3 = int(input("\nType the number corresponding to the side order you would like to select.\n")) - 1          
    
print("\nHere is our dessert menu:")

for i in range(4):
    print((str(i + 1)) + ".", " " + (str(Menu4[i][0])), "(Calories:", (str(Menu4[i][1])) + ")")

choice4 = int(input("\nType the number corresponding to the dessert you would like to select.\n")) - 1

print("All right! So in order, your combo was:\n")
print(Menu1[choice1][0], "+", Menu2[choice2][0], "+", Menu3[choice3][0], "+", Menu4[choice4][0])

totalcal = Menu1[choice1][1] + Menu2[choice1][1] + Menu3[choice1][1] + Menu4[choice1][1]

print("\nThat makes your total caloric intake for this meal:")
print(totalcal, "total calories")

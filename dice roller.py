import random

def dice_sides():
    sides_of_dice = int(input("Enter the no of sides:"))
    return sides_of_dice


def dice_number():
    no_of_dice = int(input("Enter no.of dices:"))
    return no_of_dice


def roll_dice(sides_of_dice, no_of_dice):
    dice = []
    print("sides:"+str(sides_of_dice)+" "+"dices:"+str(no_of_dice))
    for i in range(no_of_dice):
      random_roll=random.randint(1,sides_of_dice)
      dice.append(random_roll)
    return dice
def sum_dice(dice):
    total=0
    for die in dice:
        total+=die
        print("The total value of your roll is:"+str(total))
def roll_again():
    user_input=input("Want to roll again:(Y/N)").lower()
    if user_input!="y":
        roll=False
    else:
        roll=True
    return roll
print("Welcome\n")
rolling=True

while rolling:
    d_sides=dice_sides()
    d_number=dice_number()
    my_dice=roll_dice(d_sides,d_number)
    sum_dice(my_dice)
    rolling=roll_again()
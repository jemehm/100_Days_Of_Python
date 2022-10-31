import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lst = [rock, paper, scissors]

plyer=int(input("What do you choose ? Type 0 for Rock,  1 for Paper or  2 for Scissors."))

if plyer >= 3 or plyer < 0:
    print("You typed invalid number, YOU LOSE!")
else:
    print(lst[plyer])

    pc = random.randint(0,2)
    print("pc chose:")
    print(lst[pc])

    if plyer == 0 and pc ==2:
       print("You Win!")
    elif pc == 0 and plyer == 2 :
      print("you lose!")
    elif plyer < pc :
      print("you lose!")
    elif plyer > pc:
        print("you Win!")
    elif plyer== pc:
        print("it is draw")


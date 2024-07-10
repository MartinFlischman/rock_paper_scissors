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

player_hand = int(input(
    "What is your selection? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

cpu_hand = random.randint(0, 2)

if (player_hand == 0) or (player_hand == 1) or (player_hand == 2):
    print("\nThe computer chose:")
    if cpu_hand == 0:
        print(rock)
    elif cpu_hand == 1:
        print(paper)
    else:
        print(scissors)

    if cpu_hand == player_hand:
        print("\nIt's a draw!")
    elif (cpu_hand == 0 and player_hand == 1) or (cpu_hand == 1 and player_hand == 2) or (cpu_hand == 2 and player_hand == 0):
        print("\nYou win!")
    elif (cpu_hand == 1 and player_hand == 0) or (cpu_hand == 2 and player_hand == 1) or (cpu_hand == 0 and player_hand == 2):
        print("\nThe computer wins!")
else:
    print("\nYou typed an invalid character. Only type 0, 1 or 2.")

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


player_choice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")  # "2"

player = int(player_choice)  # 2

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer_choice = random.choice("123")
computer = int(computer_choice)

print("")
print(f"You chose {str(RPS(player)).replace("RPS.", "")}.")
# You chose PAPER.
print(f"Python chose {str(RPS(computer)).replace("RPS.", "")}.")
# Python chose ROCK.
print("")

result = (player, computer)

if result == (1, 3) or result == (2, 1) or result == (3, 2):
    print("🥳😜 Congrats! You win!  ") # 🥳😜 Congrats! You win!
elif player == computer:
    print("😎 It's a tie!")
else:
    print("😡 Python wins!")

# References:
# print(RPS(2))           # RPS.PAPER
# print(RPS.ROCK)         # RPS.ROCK
# print(RPS['ROCK'])      # RPS.ROCK
# print(RPS.ROCK.value)   # 1
# sys.exit()

# value = input("Please enter a your name: ")
# print(value)

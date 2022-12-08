import random
again=True
while again:
    print(random.randint(1,6))
    another_roll =input(" You want to roll the dice again? (Yes/No):")
    if another_roll.lower()=="yes":
        continue
    else:
        break

import random

user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(['rock', 'paper', 'scissors'])

print(f"You chose: {user}")
print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif (user == 'rock' and computer == 'scissors') or \
     (user == 'paper' and computer == 'rock') or \
     (user == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("Computer wins!")

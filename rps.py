# rock_paper_scissors

# 'player'
# 'computer'

# first action: computer - random pick ['rock', 'paper', 'scissors']
# second action: player - pick ['rock', 'paper', 'scissors']

# outcome:  -'Game Tied'
#           -'You Win'
#           -'You Loose'

# collect input until 'quit'
# print 'Thank you for playing!'

# options = ['rock', 'paper', 'scissors']
# random.choice(options)



import random
def rock_paper_scissors():
    while True:
        options = ['rock', 'paper', 'scissors']
        computer = random.choice(options)
        first_q = input("\nWould you like to  play 'rock, paper, scissors? ['y'/'n']: ")
        if first_q.lower().strip() == "n":
            print("Thank you for playing! ")  #---> added this line <---
            break
        player = input("\nPick rock['r'] paper['p'] scissors['s']: ")
        # if player == computer:
        #     print("\nGame Tied.")
        if computer == 'rock' and player =='s':
            print("\nYou Lose!")
        elif computer == 'rock' and player == 'p':
            print("\nYou Win!")
        elif computer == 'rock' and player == 'r':
            print("\nGame Tied.")
        elif computer == 'scissors' and player == 'r':
            print('\nYou Win!')
        elif computer == 'scissors' and player == 'p':
            print("\nYou Lose!")
        elif computer == 'scissors' and player == 's':
            print("\nGame Tied.")
        elif computer == 'paper' and player == 's':
            print("\nYou Win!")
        elif computer == 'paper' and player == 'r':
            print("\nYou Lose!")
        elif computer == "paper" and player == 'p':
            print("\nGame Tied.")
        else:
            print("I didn't know there was other options you silly goose!")
            continue

        print(f"\nYou chose {player.upper()} and the computer chose {computer.upper()}")

rock_paper_scissors()
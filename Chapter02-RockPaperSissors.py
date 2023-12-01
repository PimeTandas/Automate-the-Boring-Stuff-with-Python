import random, sys

# These variables will keep the number of wins, loses and draws.
wins = 0
losses = 0
draws = 0

# The main game loop
while True:
    print("%s Wins, %s Losses, %s Draws" % (wins, losses, draws))
    while True:
        print('Please select your move: (R)ock, (P)aper, (S)cissors, (Q)uit: ')
        userMove = input().lower()
        # Check if user wants to quit game
        if userMove == 'q':
            sys.exit()
        if userMove == 'r' or userMove == 'p' or userMove == 's':
            break
        print("Please select one of the stated options")

    # Display what the user selected
    if userMove == 'r':
        print("User selected ROCK!")
        print("Rock verses...")
    elif userMove == 'p':
        print("User selected PAPER!")
        print("Paper verses...")
    elif userMove == 's':
        print("User selected SCISSORS!")
        print("Scissors verses...")

    # Display what the computer selected
    randomNum = random.randint(1,3)
    if randomNum == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNum == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNum == 3:
        computerMove = 's'
        print("SCISSORS")

    # Display and record the Win, Losses and Draws stats
    if userMove == computerMove:
        draws += 1
        print("Its a draw!")
    elif userMove == 'r' and computerMove == 's':
        wins += 1
        print("User wins!")
    elif userMove == 'r' and computerMove == 'p':
        losses += 1
        print("Computer wins!")
    elif userMove == 'p' and computerMove == 's':
        losses += 1
        print("Computer wins!")
    elif userMove == 'p' and computerMove == 'r':
        wins += 1
        print("User wins!")
    elif userMove == 's' and computerMove == 'p':
        wins += 1
        print("User wins!")
    elif userMove == 's' and computerMove == 'r':
        losses += 1
        print("Computer wins!")
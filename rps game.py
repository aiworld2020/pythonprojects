import random
#Variables to determine how much the user has enterd r, p or s
rock = 0
paper = 0
scissors = 0

#Games computer won, games user won, and ties
ties = 0
i_won = 0
user_won = 0


while(True):
    print("We are playing a game of rock, paper scissors.")

    #asks for user's input
    user_input = input("\nEnter r for rock, p for paper, s for scissors, or q for quit :")

    #checks if input is right
    while (True):
        user_input =  user_input.lower()
        if user_input != "r" and user_input != "p" and user_input != "s" and user_input != "q":
            print("You did not enter rock, paper, scissors, or quit, try again")
            user_input = str(input("\nEnter r for rock, p for paper, s for scissors, or q for quit :"))
            continue
        else:
            break

    #program for rock

    if user_input == "r":
        if rock >= 3:
            print("I chose paper, I win")
            i_won += 1
            rock += 1
        random_number = random.randint(1,3)
        if random_number == 1:
            print("I chose rock, tie")
            ties += 1
            rock += 1
        elif random_number == 2:
            print("I chose paper, I win")
            i_won += 1
            rock += 1
        elif random_number == 3:
            print("I chose scissors, you win")
            user_won += 1
            rock += 1

    #program for paper

    elif user_input == "p":
        if paper >= 3:
            print("I chose scissors, I win")
            i_won += 1
            paper += 1
        random_number = random.randint(1,3)
        if random_number == 1:
            print("I chose rock, you win")
            user_won += 1
            paper += 1
        elif random_number == 2:
            print("I chose paper, tie")
            ties += 1
            paper += 1
        elif random_number == 3:
            print("I chose scissors, I win")
            i_won += 1
            paper += 1

    #program for scissors

    elif user_input == "s":
        if scissors >= 3:
            print("I chose rock, I win")
            i_won += 1
            scissors += 1
        random_number = random.randint(1,3)
        if random_number == 1:
            print("I chose rock, I win")
            i_won += 1
            scissors += 1
        elif random_number == 2:
            print("I chose paper, you win")
            user_won += 1
            scissors += 1
        elif random_number == 3:
            print("I chose scissors, tie")
            ties += 1
            scissors += 1

    #program for quit
    elif user_input == "q":
        print("GG")
        print("I won ", i_won ," games.")
        print("You won ", user_won ," games.")
        print("There were ",ties ," ties")
        break


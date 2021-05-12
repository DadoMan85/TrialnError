import random
import math

# Python3 DGallaway 4-28-21 Revision Date:
# just a note to leave a not about a note....... note


def main():
    name = input("What is your name?: \n")
    print("")
    print("Hello " + name)

    print("Pick a number 1 through 5\n")
    print("1: Random Question")
    print("2: Dad Jokes")
    print("3: Guess the number")
    print("4: Rock, Paper, Scissors")
    print("5: Not done yet")
    numb1 = int(input("Pick a number?: \n"))

    if numb1 == 1:
        print("Random Question!!")
        answer = int(input("How many shoes are you wearing, " + name + "?: \n"))

        if answer == 2:
            print("That is the perfect number of SHOES!")
        elif answer > 2:
            print("Always carry a spare?")
        else:
            print("Walking lopsided today, " + name + "?")

    elif numb1 == 2:
        print("Random Dad Jokes!")
        num2 = int(input("Select 1, 2, 3 or 4: \n"))
        if num2 == 1:
            joke1 = str(input("What do runner eat be a race?: \n"))
            print("")
            print("Nothing, they fast lol!")
        elif num2 == 2:
            joke2 = str(input("What rock group has four men that don't sing?: \n"))
            print("")
            print("Mount Rushmore lol!")
        elif num2 == 3:
            joke3 = str(input("How does Moses make his coffee?: \n"))
            print()
            print("Hebrews it! lol")
        else:
            joke4 = str(input("What concert costs just 45 cents?: \n"))
            print("")
            print("50 Cent, Featuring Nickelback lol!")

    elif numb1 == 3:
        count = 1
        myNumber = random.randint(1, 20)

        print("Guess the random Number!!")

        while True:
            try:
                guess = int(input("Guess a number between 1 and 20: \n"))

                while guess < 1 or guess > 20:
                    print("Error, the number is not between 1 and 20")
                    guess = int(input("Pick a number between 1 and 20: \n"))

            except ValueError:
                print("Error!")
                continue

            if guess < myNumber:
                print("Too Low")
                count = count +1
            elif guess > myNumber:
                print("Too High")
                count = count +1
            elif guess == myNumber:
                print("You guessed it in " + str(count) + " appempts!")
                break
            else:
                print("Error, Pick a number between 1 and 20: \n")

    elif numb1 == 4:
        from random import randint

        # Random # in python
        # print(randint(1, 3))

        print("Rock Paper Scissors Game\n")

        more = "y"

        while more.lower() == "y":
            print("Pick One")
            print("Pick Rock (r)")
            print("Pick Paper (p)")
            print("Pick Scissors (s)")
            choice = input("\nEnter your choice: ")
            choice = choice.lower()

            # have python choose rock, paper or scissors
            number = randint(1, 3)
            if number == 1:
                computer = "r"
            elif number == 2:
                computer = "p"
            elif number == 3:
                computer = "s"
            else:
                print("Error. Invalid computer number.")

            # check to see who wins
            if computer == "r" and choice == "r" or computer == "p" and choice == "p" or computer == "s" and choice == "s":
                print("You tied the computer")
                print("Computer: " + computer)
                print("Your choice: " + choice)

            elif computer == "r" and choice == "s" or computer == "p" and choice == "r" or computer == "s" and choice == "p":
                print("Computer wins")
                print("Computer: " + computer)
                print("Your choice: " + choice)

            elif computer == "r" and choice == "p" or computer == "p" and choice == "s" or computer == "s" and choice == "r":
                print("You win")
                print("Computer: " + computer)
                print("Your choice: " + choice)

            else:
                print("Something went wrong")

            more = input("\nDo you want to play again? (y/n): ")

        print("Goodbye!")


    else:
        print("not done yet")




if __name__ == "__main__":
    main()

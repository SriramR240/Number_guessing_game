#import necessary modules
import random
import time
import csv

#define file name here
CSV_FILE = 'highscore.csv'
DIFFICULTY = None

def get_random() -> int:
    """
    Function to generate a random whole number between and including 1 and 100.
    :return: A random whole number.
    """
    return random.randint(1,100)

def get_choice() -> int:
    """
    Get game difficulty choice from user.valid input and respective difficulty
    1-Easy ; 2-Medium ; 3-Hard
    :return: Integer denoting the no_of_tries user gets to guess the number
    """
    global DIFFICULTY
    chances = 0
    while True:
        print("Please select the difficulty level:\n1. Easy (20 chances)\n2. Medium (15 chances)")
        print("3. Hard (10 chances))\nyou have 3 hints.use them wisely")

        choice = input().lower().strip()

        if choice=='1':
            chances =20
            DIFFICULTY="easy"
        elif choice=='2':
            chances =15
            DIFFICULTY = "medium"
        elif choice=='3':
            chances =10
            DIFFICULTY = "hard"
        else:
            pass

        if chances<=0:
            print("choice invalid!")
        else:
            print(f'Great, you have selected the {DIFFICULTY} difficulty level')
            break

    return chances

def get_hint(param_guess: int,param_answer: int) -> None:
    """
    Gives the user a text hint based on the proximity of the user's guess with the
    final answer.
    :param param_guess: Integer with the latest guessed value
    :param param_answer: The value to be correctly guessed
    :return: None
    """
    diff = param_answer - param_guess

    if 0 < diff <= 20:
        print(f"you are close,{param_guess} is lesser than answer")
    elif diff>20:
        print(f"You are far away,{param_guess} is way lesser than answer")
    elif 0 > diff >= -20:
        print(f"you are close,{param_guess} is greater than answer")
    else:
        print(f"You are far away,{param_guess} is way greater than answer")

def update_high_score(score: float, param_difficulty: str) -> None:
    """
    Updates the high score in the CSV file
    :param score: Time taken to guess the answer in seconds
    :param param_difficulty:  difficulty level to check score against
    :return:
    """

    # Read the current scores from the CSV
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        print(f"File {CSV_FILE} not found")
        return

    # Check if the difficulty exists and update if necessary
    for row in rows:
        if row['difficulty'] == param_difficulty and float(row['score']) > score:
            row['score'] = str(score)
            print("New high score achieved!")

            with open(CSV_FILE, mode='w', newline='') as file:
                fieldnames = ['difficulty', 'score']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
                print(f"Scores updated successfully in {CSV_FILE}.")

if __name__ == '__main__':
    while True:
        print('''Welcome to the Number Guessing Game!\nI'm thinking of a whole number between 1 and 100''')

        answer = get_random()
        no_of_tries = get_choice()
        print("Lets start the game.!Hit H to get a hint")

        guess = None
        turns = 1
        hints = 3
        start = time.time()
        while turns<=no_of_tries:
            guess_or_hint = input("Enter your guess:").upper().strip()
            if guess_or_hint=='H':

                if hints>0:
                    if not guess:
                        print("Hey!At least guess something first!")
                    else:
                        get_hint(guess,answer)
                        guess = None
                        hints-=1
                        print(f"You have {hints} more hints")
                else:
                    print("You have run out of hints")
                continue

            try:
                guess = int(guess_or_hint)
            except ValueError:
                print("Guess is not a whole number")
                continue

            if guess==answer:
                end = time.time()
                print(f"Congrats you have guessed the number in {turns} turns")
                print(f"Total time passed:{end-start} seconds")
                update_high_score((end-start), DIFFICULTY)
                break

            print(f"Incorrect. You have {no_of_tries-turns} more chances")
            turns+=1
        else:
            print(f"{answer} was the correct number")
            print("You have run out of chances.Better luck next time")


        again = input("Enter Y to play again.else quit:").lower().strip()

        if again!='y':
            print("BYE BYE!!")
            break








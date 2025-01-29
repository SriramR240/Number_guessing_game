#import necessary modules
import random
import time
import csv

#define file name here
CSV_FILE = 'highscore.csv'
DIFFICULTY = ''
ANSWER  = 0

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
        print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)")
        print("3. Hard (3 chances))\nyou have 3 hints for all difficulties.use them wisely")

        choice = input().lower().strip()

        if choice=='1':
            chances =10
            DIFFICULTY="easy"
        elif choice=='2':
            chances =5
            DIFFICULTY = "medium"
        elif choice=='3':
            chances =3
            DIFFICULTY = "hard"
        else:
            pass

        if chances<=0:
            print("choice invalid!")
        else:
            print(f'Great, you have selected the {DIFFICULTY} difficulty level')
            break

    return chances

def get_system_hint(param_guess: int) -> None:
    """
    Gives the user a text hint based on the proximity of the user's guess with the
    final answer.
    :param param_guess: Integer with the latest guessed value
    :return: None
    """
    if param_guess>ANSWER:
        print(f"{param_guess} is greater than answer")
    else:
        print(f"{param_guess} is lesser than answer")

def get_user_hint(hint_number: int) -> None:
    """
    Gives the users hint based on hint count.for first hint - give if number is odd or even
    For second hint , give the sum of digits , for third hint give the multiplication of digits
    hint_number : the number of hints that existed when the user called for a hint
    :return: None
    """

    if hint_number == 3:
        if ANSWER % 2 ==0:
            print("It is an Even number")
        else:
            print("It is an Odd number")
    elif hint_number == 2:
        sum =0
        for i in str(ANSWER):
            sum += int(i)
        print(f"The sum of the digits is {sum}")
    else:
        mult=1
        for i in str(ANSWER):
            mult *= int(i)
        print(f"The multiplication of the digits is {mult}")

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

        ANSWER = get_random()
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
                    get_user_hint(hints)
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

            if guess==ANSWER:
                end = time.time()
                print(f"Congrats you have guessed the number in {turns} turns")
                print(f"Total time passed:{end-start} seconds")
                update_high_score((end-start), DIFFICULTY)
                break

            get_system_hint(guess)
            print(f"You have {no_of_tries-turns} more chances")
            turns+=1
        else:
            print(f"{ANSWER} was the correct number")
            print("You have run out of chances.Better luck next time")

        again = input("Enter Y to play again.else quit:").lower().strip()

        if again!='y':
            print("BYE BYE!!")
            break








import random
import time
import csv

CSV_FILE = 'highscore.csv'
difficulty = None

def get_random():
    return random.randint(1,100)

def get_choice():
    global difficulty
    chances=0
    while True:
        print('''
Please select the difficulty level:
1. Easy (20 chances)
2. Medium (15 chances)
3. Hard (10 chances))
you have 3 hints.use them wisely
            ''')
             
        choice = input().lower()
        
        match choice:
            case "1":
                chances =20
                difficulty="easy"
            case "2":
                chances =15
                difficulty = "medium"
            case "3":
                chances =10
                difficulty = "hard"
        
        if chances<=0:
            print("choice invalid!")
        else:
            print(f'Great, you have selected the {difficulty} difficulty level')
            break
        
    
    return chances


def get_hint(guess,answer):
    
    diff = answer - guess
    
    if diff>0 and diff<=20:
        print(f"you are close,{guess} is lesser than answer")
    elif diff>20:
        print(f"You are far away,{guess} is way lesser than answer")
    elif diff<0 and diff>=-20:
        print(f"you are close,{guess} is greater than answer")
    else:
        print(f"You are far away,{guess} is way greater than answer")
        


def update_high_score(score: int, difficulty: str):
    print(difficulty,score)
    updated = False
    rows = []
    
    # Read the current scores from the CSV
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        print(f"File {CSV_FILE} not found")

    # Check if the difficulty exists and update if necessary
    for row in rows:
        if row['difficulty'] == difficulty:
            if int(row['score']) > score:
                row['score'] = str(score)
                print("New high score achieved!")
                break
    # Write back to the CSV
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ['difficulty', 'score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    if updated:
        print(f"Scores updated successfully in {CSV_FILE}.")


if __name__ == '__main__':
    while True:
        print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100''')
        
        answer = get_random()

        chances = get_choice()
        print("Lets start the game!Hit H to get a hint")
        
        guess=None
        turns = 1
        hints = 3
        start = time.time()
        while turns<=chances:
            guess_or_hint = input("Enter your guess (int):").upper()
            
            if guess_or_hint=='H':
                
                if hints>0:
                    if not guess:
                        print("Hey!Atleast guess something first!")
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
            except:
                print("Guess not a valid integer")
                continue
            
            if guess==answer:
                end = time.time()
                print(f"Congrats you have guessed the number in {turns} turns")
                print(f"Total time passed:{end-start} seconds")
                update_high_score((end-start), difficulty)
                break
            
            print(f"Incorrect. You have {chances-turns} more chances")
            turns+=1
        else:
            print(f"{answer} was the correct number")
            print("You have run out of chances.Better luck next time")
            
            
        again = input("Enter Y to play again.else quit:").lower()
        
        if again!='y':
            print("BYE BYE!!")
            break
        
            
            
        
        
    


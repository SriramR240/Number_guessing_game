import random

def get_random():
    return random.randint(1,100)

def get_choice():
    chances=0
    while True:
        print('''
                  Please select the difficulty level:
                  1. Easy (10 chances)
                  2. Medium (5 chances)
                  3. Hard (3 chances))
            ''')
             
        choice = input().lower()
        difficulty = None
        
        match choice:
            case "1":
                chances =10
                difficulty="easy"
            case "2":
                chances =5
                difficulty = "medium"
            case "3":
                chances = 3
                difficulty = "hard"
        
        if chances<=0:
            print("choice invalid!")
        else:
            print(f'Great you have selected the {difficulty} difficulty level')
            break
    return chances


if __name__ == '__main__':
    while True:
        answer = get_random()
        print('''Welcome to the Number Guessing Game!
              I'm thinking of a number between 1 and 100.
              ''')
              
        chances = get_choice()
        print("Lets start the game!")
        
        for i in range(chances):
            guess = input("Enter your guess:")

            try:
                guess = int(guess)
            except:
                print("Guess not a valid integer")
                continue
            
            if guess==answer:
                print("Congrats you have guessed the number")
                break
            elif guess>answer:
                print(f"{guess} is greater than answer")
            else:
                print(f"{guess} is lesser than answer")
        else:
            print("You have run out of chances.Better luck next time")
            
            
        
        
    


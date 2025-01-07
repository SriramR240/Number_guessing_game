import random

def get_random():
    return random.randint(1,100)

def get_choice():
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
        difficulty = None
        
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
                print(f"Congrats you have guessed the number in {turns} turns")
                break
            
            print(f"Incorrect. You have {chances-turns} more chances")
            turns+=1
        else:
            print(f"{answer} for the correct number")
            print("You have run out of chances.Better luck next time")
            
            
        again = input("Enter Y to play again.else quit:").lower()
        
        if again!='y':
            print("BYE BYE!!")
            break
        
            
            
        
        
    


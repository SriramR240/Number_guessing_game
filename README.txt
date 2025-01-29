#Number Guessing Game

This is a CLI-based game, so you need to use the command line to interact with the game. The game works as follows:

##How to Play
1. The system will generate a random number between 1 and 100.
2. You will be prompted to select a difficulty level:
   - Easy: 10 chances to guess
   - Medium: 5 chances to guess
   - Hard: 3 chances to guess
3. You can guess a number or type `H` to use a hint. You have a total of 3 hints per game:
   - Hint 1: Tells whether the number is even or odd.
   - Hint 2: Provides the sum of the digits of the number.
   - Hint 3: Provides the multiplication of the digits of the number.
4. If your guess is incorrect, the system will tell you if your guess is higher or lower than the answer.
5. The game continues until you:
   - Guess the correct number (win)
   - Run out of chances (lose)
6. If you win, your time taken to guess the number will be checked against the high score for that difficulty level and updated if it's a new record.
7. After a game ends, you will have the option to play again or exit.

##Installation and Running the Game
1. Ensure you have Python installed (version 3.x recommended).
2. Download the script and save it in a directory of your choice.
3. Open a terminal and navigate to the directory where the script is saved.
4. Run the game by executing:
   ```sh
   python filename.py
   ```
   Replace `filename.py` with the actual name of the script.

##High Scores
- The game keeps track of the fastest time to guess the number for each difficulty level.
- Scores are stored in a CSV file (`highscore.csv`).
- If you beat a previous best time, the score will be updated automatically.

##Requirements
- Python 3.x
- Standard Python libraries (random, time, csv)

##Features
- Multiple difficulty levels
- Hints system
- High score tracking
- CLI-based interactive gameplay

Enjoy the game and test your guessing skills!

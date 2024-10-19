import random

hard_level = 5
easy_level = 10

answer = random.randint(1,100)

def checkAnswer(guess, answer, turns):
    if guess > answer:
        print('your answer is too high, ')
        return turns - 1
    elif guess < answer:
        print('your answer is too low, ')
        return turns - 1
    else :
        print(f'Ya, you got it, the answer was {answer}')
        return turns -1

def setDifficulty():
    difficulty = input('Specify the difficulty level,enter 0 for easy level and 1 for hard level: ')
    if difficulty == '0':
        return easy_level
    elif difficulty == '1':
        return hard_level
    else:
        return setDifficulty()

def game():
    print('Welcome to the number guessing game!😍')
    print("I'm thinking of a number between 1 and 100.")
    turns = setDifficulty()
    guess = 0
    while(guess != answer and turns != 0):
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = checkAnswer(guess, answer, turns)
    if turns == 0:
        print(f"You've run out of guesses, you lose.😖☠️  The answer was {answer}.")
        return
    else:
        print("Congratulations!!!")

game()
playAgain = int(input('Do you want to play again? , enter 0 to No and 1 to Yes: '))
if (playAgain == 1):
    game()
else:
    print('see you soon!')
    print('By👋🏻')
import random
import math

playerScore = 0
cpuScore = 0
# def howManyGames():
#     try:
#         numberOfGames = input('How many games do you want to play up to?\n')
#         convertToInt = int(numberOfGames)
#         # if not math.isnan(numberOfGames) and (type(numberOfGames) is int):
#         # if convertToInt % 1 != 0:
#         #     if isinstance(convertToInt, int):
#         # print('first: ', type(convertToInt))
#         print(f'Okay great! {convertToInt} it is!')
#         return convertToInt
#     # else:
#     except ValueError:
#         print('What you wrote is not a number.')
#         getAnswer = str(input('Do you want to try again? (yes/no)\n')).lower()
#         if(getAnswer == 'yes'):
#             howManyGames()
#         else:
#             print('Okay, have a good day')

# howManyGames()

# def howManyGames():
#         numberOfGames = input('How many games do you want to play up to?\n')
#         convertToInt = float(numberOfGames)
#         if not math.isnan(numberOfGames) and (type(numberOfGames) is float):
#         # if convertToInt % 1 != 0:
#         #     if isinstance(convertToInt, int):
#                 print(type(convertToInt))
#                 print(f'Okay great! {convertToInt} it is!')
#                 return convertToInt
#         else:
#             print('What you wrote is not a number.')
#             getAnswer = str(input('Do you want to try again? (yes/no)')).lower()
#         if(getAnswer == 'yes'):
#             howManyGames()
#         else:
#             print('Okay, have a good day')

# howManyGames()


def computerChoice():
    testing = round(random.random() * 2)
    cpuOptions = ['rock', 'paper', 'scissors']
    cpuChooses = cpuOptions[testing]
    print(type(cpuChooses))
    return cpuChooses

# print(computerChoice())

def playerChoice():
    playerChooses = int(input(f'What is your choice? \n 1 for Rock \n 2 for Paper or \n 3 for Scissors\n'))
    # print(type(playerChooses))
    if(playerChooses == 1):
        return 'rock'
    elif(playerChooses == 2):
        return 'paper'
    elif(playerChooses == 3):
        return 'scissors'
    else:
        print('Wrong number and/or Key')
        getAnswer = str(input('Do you want to try again? (Write yes/no as a your response)\n').lower()).strip()
        if(getAnswer == 'yes'):
            print(playerChoice())
        else:
            print('Have a good day.')
        
    
def letsPlayAGame():
    player = playerChoice()
    cpu = computerChoice()
    if(player == 'rock' and cpu == 'scissors' or player == 'scissors' and cpu == 'paper' or player == 'paper' and cpu == 'rock' ):
        print(f'Player chooses: {player}\n CPU chooses: {cpu}')
        print('Player wins')
        playerScore = playerScore + 1
        print(f'The score is ...\n Player: {playerScore} \n CPU: {cpuScore}')
        whoWins(playerScore)
        # write your return for playerScore to see who won the whole game 
    elif(player == cpu):
        print('It\'s a tie')
        playerChoice()
    else:
        print(f'Player chooses: {player}\n CPU chooses: {cpu}')
        print('CPU wins')
        cpuScore = cpuScore + 1
        print(f'The score is ...\n Player: {playerScore} \n CPU: {cpuScore}')
        whoWins(cpuScore)

def whoWins(currentScore):
    numOfGames = howManyGames()

    
        



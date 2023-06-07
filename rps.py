import random
import math
import sys

playerScore = 0
cpuScore = 0

def computerChoice():
    testing = round(random.random() * 2)
    cpuOptions = ['rock', 'paper', 'scissors']
    cpuChooses = cpuOptions[testing]
    # print(type(cpuChooses))
    return cpuChooses

# print(computerChoice())

def playerChoice(numOfGames):
    countGames = numOfGames
    playerChooses = int(input(f'What is your choice? \n 1 for Rock \n 2 for Paper or \n 3 for Scissors\n'))
    # print(type(playerChooses))
    if(playerChooses == 1):
        letsPlayAGame('rock', countGames)
    elif(playerChooses == 2):
        letsPlayAGame('paper', countGames)
    elif(playerChooses == 3):
        letsPlayAGame('scissors', countGames)
    else:
        print('Wrong number and/or Key')
        getAnswer = str(input('Do you want to try again? (Write yes/no as a your response)\n').lower()).strip()
        if(getAnswer == 'yes'):
            playerChoice(numOfGames)
        else:
            print('Have a good day.')

def whoWins(playerPoints, cpuPoints, numOfGames):
    global playerScore
    global cpuScore
    countGames = numOfGames
    player = playerPoints
    cpu = cpuPoints

    if player == countGames:
        print('player wins the game!')
        playerScore = 0
        cpuScore = 0
    elif cpu == countGames:
        print('cpu wins the game')
        playerScore = 0
        cpuScore = 0
    else:
        print('the game continues...')
        playerChoice(countGames)
        
    
def letsPlayAGame(ply, numOfGames):
    global playerScore
    global cpuScore
    player = ply
    countGames = numOfGames
    cpu = computerChoice()
    if(player == 'rock' and cpu == 'scissors' or player == 'scissors' and cpu == 'paper' or player == 'paper' and cpu == 'rock' ):
        playerScore += 1
        print(f'Player chooses: {player}\n CPU chooses: {cpu}')
        print('Player wins')

        print(f'The score is ...\n Player: {playerScore} \n CPU: {cpuScore}')
        whoWins(playerScore, cpuScore, countGames)
# write your return for playerScore to see who won the whole game 
    elif(player == cpu):
        print('It\'s a tie')
        playerChoice(countGames)
    else:
        cpuScore += 1
        print(f'Player chooses: {player}\n CPU chooses: {cpu}')
        print('CPU wins')
        print(f'The score is ...\n Player: {playerScore} \n CPU: {cpuScore}')
        whoWins(playerScore, cpuScore, countGames)



def howManyGames():
    try:
        numberOfGames = int(input('How many games do you want to play up to?\n'))
        # convertToInt = int(numberOfGames)
# if not math.isnan(numberOfGames) and (type(numberOfGames) is int):
# if convertToInt % 1 != 0:
# if isinstance(convertToInt, int):
# print('first: ', type(convertToInt))
        print(f'Okay great! {numberOfGames} it is!')
        print('')
        startGame = input('Do you want to start the Game? (yes/no)\n').lower()
        if(startGame == 'yes'):
            playerChoice(numberOfGames)
        else:
            toEnd = input('Are you sure? (yes/no) \n')
            if(toEnd == 'yes'):
                sys.exit()
    # else:
    except ValueError:
        print('What you wrote is not a number.')
        getAnswer = str(input('Do you want to try again? (yes/no)\n')).lower()
        if(getAnswer == 'yes'):
            howManyGames()
        else:
            print('Okay, have a good day')
howManyGames()

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



    
        



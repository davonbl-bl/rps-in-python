import random
import math
import sys

playerScore = 0
cpuScore = 0

def computerChoice():
    testing = round(random.random() * 2)
    cpuOptions = ['rock', 'paper', 'scissors']
    cpuChooses = cpuOptions[testing]
    return cpuChooses


def playerChoice(numOfGames):
    countGames = numOfGames
    playerChooses = int(input(f'What is your choice? \n 1 for Rock \n 2 for Paper or \n 3 for Scissors\n'))
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
        print('player wins the game!\n')
        playerScore = 0
        cpuScore = 0
        getAnswer = input('Do you want to play again? (yes/no)\n').lower()
        if getAnswer == 'yes':
            print('')
            howManyGames()
        else:
            print('\nHave a good day!')
            sys.exit()
    elif cpu == countGames:
        print('cpu wins the game!\n')
        playerScore = 0
        cpuScore = 0
        getAnswer = str(input('Do you want to play again? (yes/no)\n')).lower()
        if getAnswer == 'yes':
            print('')
            howManyGames()
        else:
            print('\nHave a good day!')
            sys.exit()
    else:
        print('the game continues...\n')
        playerChoice(countGames)
        
    
def letsPlayAGame(ply, numOfGames):
    global playerScore
    global cpuScore
    player = ply
    countGames = numOfGames
    cpu = computerChoice()
    print('')
    if(player == 'rock' and cpu == 'scissors' or player == 'scissors' and cpu == 'paper' or player == 'paper' and cpu == 'rock' ):
        playerScore += 1
        print(f'Player chooses: {player} \nCPU chooses: {cpu}\n')
        # print('')
        print('Player wins')

        print(f'\nThe score is ...\n Player: {playerScore} \n CPU: {cpuScore}\n')
        whoWins(playerScore, cpuScore, countGames)
    elif(player == cpu):
        print('It\'s a tie\n')
        playerChoice(countGames)
    else:
        cpuScore += 1
        print(f'Player chooses: {player}\n CPU chooses: {cpu}\n')
        # print('')
        print('CPU wins')
        print(f'The score is ...\n Player: {playerScore} \n CPU:{cpuScore}\n')
        whoWins(playerScore, cpuScore, countGames)



def howManyGames():
    try:
        print('')
        numberOfGames = int(input('How many games do you want to play up to?\n'))
        print('')
        print(f'Okay great! {numberOfGames} it is!')
        print('')
        playerChoice(numberOfGames)
        # startGame = input('Start the Game? (yes/no)\n').lower()
        # if(startGame == 'yes'):
        #     print('')
        #     playerChoice(numberOfGames)
        # elif(startGame == 'no'):
        #     toEnd = input('Are you sure? (yes/no) \n')
        #     if(toEnd == 'yes'):
        #         sys.exit()
        #     else:
        #         print('')
        # else:
    except ValueError:
        print('')
        print('What you wrote is not a number.')
        print('')
        getAnswer = str(input('Do you want to try again? (yes/no)\n')).lower()
        if(getAnswer == 'yes'):
            print('')
            howManyGames()
        else:
            print('')
            print('Okay, have a good day')
howManyGames()





    
        



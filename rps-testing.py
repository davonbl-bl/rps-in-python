import random

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
    if playerChooses == 1:
        letsPlayAGame('rock', countGames)
    elif playerChooses == 2:
        letsPlayAGame('paper', countGames)
    elif playerChooses == 3:
        letsPlayAGame('scissors', countGames)
    else:
        print('Wrong number and/or Key')
        getAnswer = str(input('Do you want to try again? (Write yes/no as your response)\n').lower().strip())
        if getAnswer == 'yes':
            playerChoice()
        else:
            print('Have a good day.')

def whoWins(playerPoints, cpuPoints, numOfGames):
    global playerScore
    global cpuScore
    countGames = numOfGames
    player = playerPoints
    cpu = cpuPoints

    if player == countGames:
        print('Player wins the game!')
        playerScore = 0
        cpuScore = 0
    elif cpu == countGames:
        print('CPU wins the game')
        playerScore = 0
        cpuScore = 0
    else:
        print('The game continues...')
        playerChoice()

def letsPlayAGame(ply, numOfGames):
    global playerScore
    global cpuScore
    player = ply
    countGames = numOfGames
    cpu = computerChoice()
    if (player == 'rock' and cpu == 'scissors') or (player == 'scissors' and cpu == 'paper') or (player == 'paper' and cpu == 'rock'):
        playerScore += 1
        print(f'Player chooses: {player}\nCPU chooses: {cpu}')
        print('Player wins')
        print(f'The score is ...\nPlayer: {playerScore}\nCPU: {cpuScore}')
        whoWins(playerScore, cpuScore, countGames)
    elif player == cpu:
        print('It\'s a tie')
        playerChoice()
    else:
        cpuScore += 1
        print(f'Player chooses: {player}\nCPU chooses: {cpu}')
        print('CPU wins')
        print(f'The score is ...\nPlayer: {playerScore}\nCPU: {cpuScore}')
        whoWins(playerScore, cpuScore, countGames)

def howManyGames():
    try:
        numberOfGames = int(input('How many games do you want to play up to?\n'))
        print(f'Okay great! {numberOfGames} it is!')
        startGame = input('Do you want to start the Game? (yes/or)\n').lower()
        if startGame == 'yes':
            playerChoice(numberOfGames)
    except ValueError:
        print('What you wrote is not a number.')
        getAnswer = str(input('Do you want to try again? (yes/no)\n')).lower()
        if getAnswer == 'yes':
            return howManyGames()
        else:
            print('Okay, have a good day')

howManyGames()
import random
import math

def howManyGames():
    try:
        numberOfGames = input('How many games do you want to play up to?\n')
        convertToInt = int(numberOfGames)
        # if not math.isnan(numberOfGames) and (type(numberOfGames) is int):
        # if convertToInt % 1 != 0:
        #     if isinstance(convertToInt, int):
        print(type(convertToInt))
        print(f'Okay great! {convertToInt} it is!')
        return convertToInt
    # else:
    except:
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


def computerChoice():
    testing = round(random.random() * 2)
    cpuOptions = ['rock', 'paper', 'scissors']
    cpuChooses = cpuOptions[testing]
    print(type(cpuChooses))
    return cpuChooses

print(computerChoice())

# def playerChoice():
#     playerChooses = int(input(f'What is your choice? \n 1 for Rock \n 2 for Paper or \n 3 for Scissors\n'))
#     # print(type(playerChooses))
#     if(playerChooses == 1):
#         return 'rock'
#     elif(playerChooses == 2):
#         return 'paper'
#     elif(playerChooses == 3):
#         return 'scissors'
#     else:
#         print('Wrong number and/or Key')
#         getAnswer = str(input('Do you want to try again? (Write yes/no as a your response)\n').lower()).strip()
#         if(getAnswer == 'yes'):
#             print(playerChoice())
#         else:
#             print('Have a good day.')
        
    
# print(playerChoice())


    
        



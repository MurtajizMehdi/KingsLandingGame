# Murtajiz Mehdi
# August 3, 2021
# Group project

# Create first function which is introduction
def ProgramIntro():
    print(30 * '*')
    print('WELCOME TO OUR GAME!!')
    print(30 * '*')
    # These "crosses" represent medieval times, I figured it would fit the theme better


# Create function that'll be used whenever the player chooses the wrong option and has to start over or quit
def PlayerDied():
    answer = ''
    print('YOU DIED!!')
    answer = input('Would you like to play again? yes or no: ')
    if answer == 'yes':
        FinishedGame()  # This should take them back to the menu once they hit 1
    else:
        print('Thank you for playing, take care...')  # This should exit the user from the game


# Create first question function
def GameQuestionOne():
    answer = 0
    print('A knight in shining armor approaches you, noticing you are lost.')
    answer = int(input('Will you take his guidance? 1) yes 2) no: '))
    if answer == 1:
        print('The Knight was an imposter! He lures you in and kills you.')
        PlayerDied()
    elif answer == 2:
        print('\nThe "knight" was actually a deranged imposter who ambushed a REAL knight.')
        print('Good thing you ran off!')
    else:
        print('Please choose "1" or "2".')
        GameQuestionOne()


# Create second question function
def GameQuestionTwo():
    answer = 0
    print('After running away from the imposter, you reach a seemingly bottomless ravine.')
    answer = int(input(
        'You see a bridge that leads to the other side. Do you... 1) take the bridge,'
        ' or 2) slide down the mountain and go through the ravine: '))
    if answer == 1:
        print("The bridge's ropes give out, and the bridge collapses!")
        PlayerDied()
    elif answer == 2:
        print('\nYou notice the ropes at the other side were very flimsy, you made the right call.')
    else:
        print('Please choose "1" or "2".')
        GameQuestionTwo()


# Create third question function
def GameQuestionThree():
    answer = 0
    print('As you walk through the ravine, you notice your leg took some damage on the way down.')
    answer = int(input(
        'You see that there is a flatrock located to your right. Do you... 1) Sit down and take a break, or 2) tough it out and keep walking: '))
    if answer == 1:
        print('The rock is being held up on a pole and leads to a subterranean tunnel filled with golems!')
        PlayerDied()
    elif answer == 2:
        print('\nYou notice that after a while of walking, the rock disappears without a trace...')
    else:
        print('Please choose "1" or "2".')
        GameQuestionThree()


# Create fourth question function
def GameQuestionFour():
    answer = 0
    print('After making it out of the ravine, you finally see a giant castle...')
    print(
        'The king notices your scars and injuries and approaches you and honors your bravery and courage,'
        ' he praises you...')
    print('He offers you the divine right to rule with him...')
    answer = int(input(
        'Do you... 1) reject the offer and try to assassinate the king for his crimes against your people,'
        ' or 2) take it and join the king: '))
    if answer == 1:
        print(
            '\nThe king stops you in your tracks with his mighty strength,'
            ' and proceeds to take you in to his castle with your hands tied up.')
    elif answer == 2:
        print('As you walk with the King to your throne, you start telling him about your journey...')
        print('You tell him about the "knight" that tried to kill you...')
        print('He stops you, and describes the Knight in very detailed fashion...')
        print(
            'He tells you that the "Knight" is actually his jealous youngest son who was not chosen to be the heir...')
        print(
            'The son has been following you all along!'
            ' He runs up behind you and impales you so the King will have no choice but to let him rule')
        PlayerDied()
    else:
        print('Please choose "1" or "2".')
        GameQuestionFour()


# create fifth question function
def GameQuestionFive():
    answer = 0
    print('The king respects your ambition and drive for your people...')
    print('After talking to the King, you understand that he is not such a bad guy...')
    print('A lot of the things he did were for the better for the land, unfortunately some people had to suffer.')
    answer = int(input(
        'He cuts the ropes off your hands, and reaches out to shake them, do you...'
        ' 1) Shake them and accept the offer, or 2) slap his hand away.'))
    if answer == 1:
        print('\nYou two bring peace to your land as you co-rule with the king. '
              'Your people are suffering no longer. Rejoice!')
    elif answer == 2:
        print('The king is now fed up with your antics. He feeds you to his dragon.')
        PlayerDied()
    else:
        print('Please choose "1" or "2".')
        GameQuestionFive()


# Create function that has all questions in one
def MainGame():
    answer = 0
    GameQuestionOne()

    GameQuestionTwo()

    GameQuestionThree()

    GameQuestionFour()

    GameQuestionFive()

    print('Great job, you made it!')
    answer = int(input('Would you like to play again? 1) Yes 2) No: '))
    if answer == 1:
        FinishedGame()
    elif answer == 2:
        print('Thank you for playing, take care adventurer!!')


def TitleScreen():
    Tschoice = 0
    print('+x+x+x+x+x+x+x+x+x+x+x+x+x+')
    print("WELCOME TO KING'S LANDING!!")
    print('+x+x+x+x+x+x+x+x+x+x+x+x+x+')
    print('\n\n')


    print('*PLEASE CHOOSE NUMERICAL VALUES FOR EACH CHOICE*')
    print('1) PLAYER 1 GAME\n2) ABOUT\n3) RULES\n4) CREDITS\n5) EXIT\n')
    Tschoice = int(input('Please choose what you would like to do: '))


    if Tschoice == 1:
        print('\nYou are a peasant boy who comes from a very poor village...')
        print('You and your people have grown resentment for the King of the land...')
        print("Having witnessed your people suffer, you venture out into the forest without")
        print("the slightest clue of where you're supposed to be going...")
        MainGame()  # Prompts game questions

    elif Tschoice == 2:
        print("King's Landing is a game about surviving until you reach your destination.")
        print("You'll run into all sorts of things and problems... good luck!!\n\n")
        FinishedGame()  # Prompts the entire game itself

    elif Tschoice == 3:
        print('The rules are simple!\n\n')
        print('1. For each question within the game, answer with a "1" or "2".')
        print('2. If you error out, enter "FinishedGame()".')
        print('3. Have fun!!')

    elif Tschoice == 4:
        print('This awesome game was thought up and created by Murtajiz Mehdi and Andrew Robertoy.\n\n')
        FinishedGame()  # Prompts the entire game itself

    elif Tschoice == 5:
        print('Have a great day, we hope to see you soon!')


# Prompting the title screen already contains the main game within it
# Only need to display the outro
def FinishedGame():
    TitleScreen()
    print('Thank you for playing our game, we hope you had fun. Until next time, so long adventurer!')


FinishedGame()
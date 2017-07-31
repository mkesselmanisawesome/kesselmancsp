# -*- coding: utf-8 -*-
import random

def zombie_dice():
    #print('\033[H\033[J')  clear screen code that isn't working as I like but I am saving for now.
    #Introduction for the game with how to play is here.
    print '\n'
    print 'Welcome to Zombie Dice solitaire.  You can either roll brains, shotguns or feet.'
    print 'You win once you get 5 brains.  Once you have rolled 3 shotguns, you'
    print 'lose all your brains and have to start again.  If you roll feet, one'
    print 'of your victims escapes and you will lose a brain.'
    print
    
    rollcount = 0         #This section initializes all variables to 0.
    brain = 0
    shotgun = 0
                       
    while brain < 5:                #They have to have 5 brains to win so this while loop will go until then.
        roll = random.randint(1,4)  #Randomly rolls an integer 1, 2, 3 or 4.  I included two options to get brains because I felt it took to long to win otherwise.
        rollcount += 1              #This is a counter to keep track of how many rolls it takes for the player to win. This increases count by 1.
        if roll == 1 or roll == 4:  #A roll of 1 or 4 counts as a brain.
            print 'You rolled a brain.'
            print
            brain += 1             #This increases the brain count by 1.
        elif roll == 2:            #A roll of 2 counts as a shotgun.
            print 'You rolled a shotgun. If you roll 3 shotguns you lose all of your brains!'
            print
            shotgun += 1           #This increases the shotgun count by 1.
            if shotgun == 3:       #If they accumulate 3 shotguns, their brains resets to 0 and they have to work to get 5 brains again.
                print 'Oh no, that was your 3rd shotgun, you lost all your brains!'
                shotgun = 0        #Here shotguns and brains are both reset to 0.
                brain = 0
        elif roll == 3:            #A roll of 3 counts as feet where the player loses a brain.
            print 'You rolled feet...one of your victims escaped so you lose a brain from your total.'
            print 'Don\'t worry, you can\'t have less than 0 brains!'
            print
            if brain != 0:         #This makes it so that they cannot have negative brains.
                brain -= 1          #This takes a brain away from their score.
        print 'You have ' + str(brain) + ' brain(s) and ' + str(shotgun) + ' shotgun(s).'  #This allows the player to know their current score.
        print
        if brain < 5:
            raw_input('Press enter to roll again')   #This pauses so the player can see their score before they roll again.
            print
    print 'You finally got all your brains for an awesome weekend snack! It took you ' + str(rollcount) +' rolls to win!'
    #The above line is for the end of the game and lets the player know how many rolls it took for them to win.
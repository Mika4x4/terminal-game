print('terminal_game loading...')

# Game variables
health = 4
inventory = ''

#INTRODUCTION
name = input('\nEnter your name: ')
print(f'\nHello {name}, welcome to the Terminal Game!')
print('In this game, you will make choices that affect your health and inventory.')
print('Before we begin , here are your starting stats:')
print(f'\n\033[31mHEALTH :{health}\033[0m')
print(f'\033[31mINVENTORY :{inventory}\033[0m')
input('\nPress Enter to continue...')


print('\n\033[96mYou wake up to find yourself in a dark and dangerous cave. The air is thick and the ground is uneven.\033[0m')
print('\033[96mYour goal is to safely navigate your way through the cave and find your way out.\033[0m')

input('\nPress Enter to continue...')


#CHOICE 1
print('\n\033[38;5;205mDo you search the area you are in (1) or move forward into the darkness (2):\033[0m')
choice1 = input('Choose an option (1 or 2): ')

#CHOICE 1 CONSEQUENCES
while choice1 != '1' and choice1 != '2':
    print('\nInvalid choice. Please choose 1 or 2.')
    choice1 = input('Choose an option (1 or 2): ')

if choice1 == '1':
    print('\n\033[96mYou search the area and find a flashlight and a broken glass bottle.\033[0m')
    print('\033[96mYou pick up the items and add them to your inventory.\033[0m')
    inventory = 'flashlight, broken glass bottle'
    print(f'\n\033[31mHEALTH :{health}\033[0m')
    print(f'\033[31mINVENTORY :{inventory}\033[0m')

elif choice1 == '2':
    print('\n\033[96mYou move forward into the darkness and suddenly fall into a pit!\033[0m')
    health = health - 1
    print('\033[96mYou lose 1 health point.\033[0m')
    print(f'\n\033[31mHEALTH :{health}\033[0m')
    print(f'\033[31mINVENTORY :{inventory}\033[0m')
input('\nPress Enter to continue...')


#LUCKY_ITEM CHOICE

print('\n\033[38;5;205mchoose an item that you may use later : slingshot (1) or basket of berries (2):\033[0m')
lucky_item = input('Choose an option (1 or 2): ')

while lucky_item != '1' and lucky_item != '2' :
    print('\nInvalid choice. Please choose 1 or 2.')
    lucky_item = input ('Choose an option (1 or 2): ')

#CHOICE 1 CONSEQUENCES CONTINUED

if choice1 == '1':
    print('\n\033[96mYou light the flashlight and notice a pit in front of you.\033[0m')
    print('\033[96mYou carefully go around the pit and continue down the path.\033[0m')
    print('\033[96mAs you walk further, you come across a bear blocking your path.\033[0m')
elif choice1 == '2':
    print('\n\033[96mYou climb out of the pit and continue down the path.\033[0m')
    print('\033[96mYou find a flashlight along the way and use it to light the path.\nfalling down pits isnt very fun\033[0m')
    print('\033[96mAs you walk further, you come across a bear blocking your path.\033[0m')
    inventory = 'flashlight'

input('\nPress Enter to continue...')

#CHOICE 2

if choice1 == '1' and lucky_item == '1':
    inventory = 'flashlight, broken glass bottle, slingshot'
    print(f'\n\033[31mINVENTORY :{inventory}\033[0m')
    print('\n\033[38;5;205mChoose an item to deal with the bear: flashlight (1) or broken glass bottle (2) or slingshot (3):\033[0m')
    choice2 = input('Choose an option (1, 2 or 3): ')
    while choice2 != '1' and choice2 != '2' and choice2 != '3':
        print('\nInvalid choice. Please choose 1, 2 or 3.')
        choice2 = input('Choose an option (1, 2 or 3): ')

elif choice1 == '1' and lucky_item == '2':
    inventory = 'flashlight, broken glass bottle, basket of berries'
    print(f'\n\033[31mINVENTORY :{inventory}\033[0m')
    print('\n\033[38;5;205mChoose an item to deal with the bear: flashlight (1) or broken glass bottle (2) or basket of berries (3):\033[0m')
    choice2 = input('Choose an option (1, 2 or 3): ')
    while choice2 != '1' and choice2 != '2' and choice2 != '3':
        print('\nInvalid choice. Please choose 1, 2 or 3.')
        choice2 = input('Choose an option (1, 2 or 3): ')

elif choice1 == '2' and lucky_item == '1':
    inventory = 'flashlight, slingshot'
    print(f'\n\033[31mINVENTORY :{inventory}\033[0m')
    print('\n\033[38;5;205mChoose an item to deal with the bear: flashlight (1) or slingshot (2):\033[0m')
    choice2 = input('Choose an option (1 or 2): ')
    while choice2 != '1' and choice2 != '2':
        print('\nInvalid choice. Please choose 1 or 2.')
        choice2 = input('Choose an option (1 or 2): ')

elif choice1 == '2' and lucky_item == '2':
    inventory = 'flashlight, basket of berries'
    print(f'\n\033[31mINVENTORY :{inventory}\033[0m')
    print('\n\033[38;5;205mChoose an item to deal with the bear: flashlight (1) or basket of berries (2):\033[0m')
    choice2 = input('Choose an option (1 or 2): ')
    while choice2 != '1' and choice2 != '2':
        print('\nInvalid choice. Please choose 1 or 2.')
        choice2 = input('Choose an option (1 or 2): ')


#CHOICE2 CONSEQUENCES

#if choice1 == 1 (flashlight and broken glass) and lucky item == 1 (slingshot) choice2 == 1 (flashlight): 
if choice1 == '1' and lucky_item == '1' and choice2 == '1' :
    print('\n\033[96mYou shine the flashlight at the bear, but this does nothing.\033[0m')
    print('\033[96mseriously what did you expect?.\033[0m')
    health = health - 3
    print('\033[96mThe bear attacks you and you lose 3 health points.\033[0m')
    if health <= 0:
        print('\n\033[31mGame Over.\033[0m')
        exit()
    else:
        print(f'\n\033[31mHEALTH :{health}\033[0m')
        print(f'\033[31mINVENTORY :{inventory}\033[0m')

#elif choice1 == 1 (flashlight and broken glass) and lucky item == 1 (slingshot) choice2 == 2 (broken glass):
elif choice1 == '1' and lucky_item == '1' and choice2 == '2' :
    print('\n\033[96mYou pierce the bear with the broken glass bottle and it runs away.\033[0m')
    print('\033[96mYou have successfully dealt with the bear.\033[0m')
    print(f'\n\033[31mHEALTH :{health}\033[0m')
    print(f'\033[31mINVENTORY :{inventory}\033[0m')

#elif choice1 == 1 (flashlight and broken glass) and lucky item == 1 (slingshot) choice2 == 3 (slingshot):
elif choice1 == '1' and lucky_item == '1' and choice2 == '3' :
    print('\n\033[96mYou shoot the bear with the slingshot, but it only makes it angry.\033[0m')
    health = health - 4
    print('\033[96mThe bear attacks you and you lose 4 health points.\033[0m')
    if health <= 0:
        print('\n\033[31mGame Over.\033[0m')
        exit()
    else:
        print(f'\n\033[31mHEALTH :{health}\033[0m')
        print(f'\033[31mINVENTORY :{inventory}\033[0m')

#elif choice1 == 1 (flashlight and broken glass) and lucky item == 2 (basket of berries) choice2 == 1 (flashlight):
elif choice1 == '1' and lucky_item == '2' and choice2 == '1' :
    print('\n\033[96mYou shine the flashlight at the bear, but this does nothing.\033[0m')
    print('\033[96mseriously what did you expect?.\033[0m')
    health = health - 3
    print('\033[96mThe bear attacks you and you lose 3 health points.\033[0m')
    if health <= 0:
        print('\n\033[31mGame Over.\033[0m')
        exit()
    else:
        print(f'\n\033[31mHEALTH :{health}\033[0m')
        print(f'\033[31mINVENTORY :{inventory}\033[0m')


#elif choice1 == 1 (flashlight and broken glass) and lucky item == 2 (basket of berries) choice2 == 2 (broken glass):
elif choice1 == '1' and lucky_item == '2' and choice2 == '2' :
    print('\n\033[96mYou pierce the bear with the broken glass bottle and it runs away.\033[0m')
    print('\033[96mYou have successfully dealt with the bear.\033[0m')
    print(f'\n\033[31mHEALTH :{health}\033[0m')
    print(f'\033[31mINVENTORY :{inventory}\033[0m')


#elif choice1 == 1 (flashlight and broken glass) and lucky item == 2 (basket of berries) choice2 == 3 (basket of berries):
elif choice1 == '1' and lucky_item == '2' and choice2 == '3' :
    print('\n\033[96mYou offer the basket of berries to the bear, which calms it down.\033[0m')
    print('\033[96mThe bear eats the berries and allows you to pass safely.\033[0m')
    print(f'\n\033[31mHEALTH :{health}\033[0m')
    print(f'\033[31mINVENTORY :{inventory}\033[0m')

 
#elif choice1 == 2 (flashlight) and lucky item == 1 (slingshot) choice2 == 1 (flashlight):
elif choice1 == '2' and lucky_item == '1' and choice2 == '1' :
    print('\n\033[96mYou shine the flashlight at the bear, but this does nothing.\033[0m')
    print('\033[96mseriously what did you expect?.\033[0m')
    health = health - 3
    print('\033[96mThe bear attacks you and you lose 3 health points.\033[0m')
    if health <= 0:
        print('\n\033[31mGame Over.\033[0m')
        exit()
    else:
        print(f'\n\033[31mHEALTH :{health}\033[0m')
        print(f'\033[31mINVENTORY :{inventory}\033[0m')

#elif choice1 == 2 (flashlight) and lucky item == 1 (slingshot) choice2 == 2 (slingshot):
elif choice1 == '2' and lucky_item == '1' and choice2 == '2' :
    print('\n\033[96mYou shoot the bear with the slingshot, but it only makes it angry.\033[0m')
    health = health - 4
    print('\033[96mThe bear attacks you and you lose 4 health points.\033[0m')
    if health <= 0:
        print('\n\033[31mGame Over.\033[0m')
        exit()
    else:
        print(f'\n\033[31mHEALTH :{health}\033[0m')
        print(f'\033[31mINVENTORY :{inventory}\033[0m')

#elif choice1 == 2 (flashlight) and lucky item == 2 (basket of berries) choice2 == 1 (flashlight):
elif choice1 == '2' and lucky_item == '2' and choice2 == '1' :
    print('\n\033[96mYou shine the flashlight at the bear, but this does nothing.\033[0m')
    print('\033[96mseriously what did you expect?.\033[0m')
    health = health - 3
    print('\033[96mThe bear attacks you and you lose 3 health points.\033[0m')
    if health <= 0:
        print('\n\033[31mGame Over.\033[0m')
        exit()
    else:
        print(f'\n\033[31mHEALTH :{health}\033[0m')
        print(f'\033[31mINVENTORY :{inventory}\033[0m')

#elif choice1 == 2 (flashlight) and lucky item == 2 (basket of berries) choice2 == 2 (basket of berries):
elif choice1 == '2' and lucky_item == '2' and choice2 == '2' :
    print('\n\033[96mYou offer the basket of berries to the bear, which calms it down.\033[0m')
    print('\033[96mThe bear eats the berries and allows you to pass safely.\033[0m')
    print(f'\n\033[31mHEALTH :{health}\033[0m')
    print(f'\033[31mINVENTORY :{inventory}\033[0m')


#CHOICE 3

input('Press Enter to continue...')

print('\n\033[96mYou continue walking and come to a fork in the path\033[0m')
print('\033[96mTo the left, you hear something. To the right, the air feels heavy.\033[0m')
print('\n\033[38;5;205mDo you go left (1) or right (2):\033[0m')
choice3 = input('Choose an option (1 or 2): ')  

#CHOICE3 CONSEQUENCES

while choice3 != '1' and choice3 != '2':
    print('\nInvalid choice. Please choose 1 or 2.')
    choice3 = input('Choose an option (1 or 2): ')

if choice3 == '1':
    print('\n\033[96mYou choose to go left and find a running stream leading out of the cave.\033[0m')
    print('\033[96mCongratulations, you have successfully navigated the cave and found your way out!\033[0m')
    input('\nPress Enter to continue...')
    print('\n\033[92mYou Win!\033[0m')
    print(f'\n\033[31mHEALTH :{health}\033[0m')
    print(f'\033[31mINVENTORY :{inventory}\033[0m')
elif choice3 == '2':
    print('\n\033[96mYou choose to go right but the air only gets heavier and you run out of breath.\033[0m')
    print('\033[96mYou collapse from lack of oxygen and die.\033[0m')
    input('\nPress Enter to continue...')
    print('\n\033[31mGame Over.\033[0m')
    

print(f'\nThank you for playing the Terminal Game {name}!')

(input('\nPress Enter to exit...'))


#RESET = '\033[0m'
#CYAN  = '\033[96m'          
#WHITE = '\033[97m'          
#RED   = '\033[31m'          
#GREEN = '\033[92m'         
#PINK  = '\033[38;5;135m'    

#Needs testing!!!
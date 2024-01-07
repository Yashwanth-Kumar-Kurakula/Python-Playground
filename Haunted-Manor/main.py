from random import randint

print('THE HAUNTED MANOR')
i_am_brave = True
score = 0

# main loop

while i_am_brave:
    ghost_door = randint(1, 3)
    print('You find yourself facing three doors...')
    print('Behind which is the ghost?')
    print('What door do you open?')
    door = input('1, 2 or 3? ')
    door_number = int(door)

    if door_number == ghost_door:
        print('A GHOST!')
        i_am_brave = False
    else:
        print('No ghost!')
        print('You enter the next room.')
        score += 1

from random import randint

print('THE HAUNTED MANOR')
i_am_brave = True
score = 0

# Main loop
while i_am_brave:
    ghost_door = randint(1, 3)
    print('You find yourself facing three doors...')
    print('Behind which is the ghost?')
    print('What door do you open?')

    door = input('1, 2 or 3? ')
    
    try:
        door_number = int(door)
        
        if door_number < 1 or door_number > 3:
            print('\nPlease enter a valid door number (1, 2, or 3).')
            continue  # Ask for input again in case of an invalid door number

        if door_number == ghost_door:
            print('\nA GHOST!')
            i_am_brave = False

        else:
            print('\nNo ghost!')
            print('You enter the next room.')
            score += 1
            
    except ValueError:
        print('\nPlease enter a valid integer.')

print('Help!')
print('Game over! Your score:', score)

# CCC 2011 J4 Boring Business
# Tissan Kugathas
# ICS4U0
# September 16 2019

# These function bellow are for the movement for the drill
# This function is for the drill to go down
def move_down(units):
    # global variables so the variable can work outside the function
    # Go down to see what each variable does
    global current_colum
    global current_row
    global loop
    global loop2
    global bool_break
    global zero_position
    # this empty string variable sets the status if the new position is safe or not
    status = ''
    # This for marks which ever place is drilled and runs for the amount units the user wants to go
    for units in range(units):
        # this makes the drill go down further
        current_colum += 1
        #  if the current spot is already drilled, then it will place x
        if underground[current_colum][current_row] == 'X':
            # sets the status to danger as it is dangerous
            status = 'DANGER'
            # this breaks the code and stops the loop from processing further more
            bool_break = True
        # this sets a drilled mark on the current spot
        underground[current_colum][current_row] = 'X'
    # After it goes through all the units and the status is yet to be set
    # it will set the status to safe
    if status == '':
        status = 'safe'
    # if the current loop is the second main loop then it will print if the drilled part is safe or not
    if loop2:
        colum = (current_colum + 1) * -1
        row = current_row - zero_position
        print(row, colum, status)

# This function is for the drill to go up
def move_up(units):
    # global variables so the variable can work outside the function
    # Go down to see what each variable does
    global current_colum
    global current_row
    global loop
    global loop2
    global bool_break
    global zero_position
    # this empty string variable sets the status if the new position is safe or not
    status = ''
    # This for marks which ever place is drilled and runs for the amount units the user wants to go
    for units in range(units):
        # This makes the drill go up
        current_colum -= 1
        #  if the current spot is already drilled, then it will place x
        if underground[current_colum][current_row] == 'X':
            # sets the status to danger as it is dangerous
            status = 'DANGER'
            # this breaks the code and stops the loop from processing further more
            bool_break = True
        # this sets a drilled mark on the current spot
        underground[current_colum][current_row] = 'X'
    # After it goes through all the units and the status is yet to be set
    # it will set the status to safe
    if status == '':
        status = 'safe'
    # if the current loop is the second main loop then it will print if the drilled part is safe or not
    if loop2:
        colum = (current_colum + 1) * -1
        row = current_row - zero_position
        print(row, colum, status)
        
# This fucntion is to make drill go to the right
def move_right(units):
    # global variables so the variable can work outside the function
    # Go down to see what each variable does
    global current_colum
    global current_row
    global loop
    global loop2
    global bool_break
    global zero_position
    # this empty string variable sets the status if the new position is safe or not
    status = ''
    # This for marks which ever place is drilled and runs for the amount units the user wants to go
    for units in range(units):
        # This makes the drill go to the right
        current_row += 1
        #  if the current spot is already drilled, then it will place x
        if underground[current_colum][current_row] == 'X':
            # sets the status to danger as it is dangerous
            status = 'DANGER'
            # this breaks the code and stops the loop from processing further more
            bool_break = True
        # this sets a drilled mark on the current spot
        underground[current_colum][current_row] = 'X'
    # After it goes through all the units and the status is yet to be set
    # it will set the status to safe
    if status == '':
        status = 'safe'
    # if the current loop is the second main loop then it will print if the drilled part is safe or not
    if loop2:
        colum = (current_colum + 1) * -1
        row = current_row - zero_position
        print(row, colum, status)

# This function is for the drill to go left
def move_left(units):
    # global variables so the variable can work outside the function
    # Go down to see what each variable does
    global current_colum
    global current_row
    global loop
    global loop2
    global bool_break
    global zero_position
    # this empty string variable sets the status if the new position is safe or not
    status = ''
    # This for marks which ever place is drilled and runs for the amount units the user wants to go
    for units in range(units):
        # This makes the drill go left
        current_row -= 1
        #  if the current spot is already drilled, then it will place x
        if underground[current_colum][current_row] == 'X':
            # sets the status to danger as it is dangerous
            status = 'DANGER'
            # this breaks the code and stops the loop from processing further more
            bool_break = True
        # this sets a drilled mark on the current spot
        underground[current_colum][current_row] = 'X'
    # After it goes through all the units and the status is yet to be set
    # it will set the status to safe
    if status == '':
        status = 'safe'
    # if the current loop is the second main loop then it will print if the drilled part is safe or not
    if loop2:
        colum = (current_colum + 1) * -1
        row = current_row - zero_position
        print(row, colum, status)

# This list represent the underground
underground = []
# This list contains the directions to get to the start
start_direction = ['d','r','d','r','u','r','d','l','u']
# This list contains the units to get to the start
start_units = [2,3,2,2,2,2,4,8,2]
# This will contain the user's direction
user_direction = []
# This will contain the user's units
user_units = []
# This loop is reponsible for being True until the user is done inputing all the inputs
loop = True
# This loop is to check if the second main loop is running
loop2 = False
# This bool will break the code if true
bool_break = False
# This is the width of the underground
width = 401
# This is the height of the underground
height = 200

# This creates the underground grid
for colum in range(height):
    underground.append([])
    for row in range(width):
        underground[colum].append([])
        
# This gets the zero position of the underground
zero_position = width//2

# This prints the chart of the underground
# It is better if the width and heigh are smaller to see the chart
##for colum in underground:
##    print(colum)

# This sets the current spot of the drill and sets X to state it is drilled
current_colum = 0
current_row = zero_position
underground[current_colum][current_row] = 'X'

# This loop allows the drill to the start position
for move in range(len(start_direction)):
    if start_direction[move] == 'd':
        move_down(start_units[move])
    elif start_direction[move] == 'r':
        move_right(start_units[move])
    elif start_direction[move] == 'l':
        move_left(start_units[move])
    elif start_direction[move] == 'u':
        move_up(start_units[move])
    
# This prints the chart of the underground
# It is better if the width and heigh are smaller to see the chart
##for colum in underground:
##    print(colum)

# This bool tells the code that the code will now proceed to the second loop      
loop2 = True
# This tracks of the number moves the drill made
move = 0

# This a while loop which asks the user to input the coordinates
# It will stop if the user enters a 'q' or if the input they inputed last is dangerous 
while loop:
    user_input = input('Enter Directions and units: ')
    # splits the user input 
    input_split = user_input.split()
    if input_split[0] == 'q':
        # Stops the loop
        loop = False
        break
    else:
        # puts the user input into the user list
        user_direction.append(input_split[0])
        user_units.append(int(input_split[1]))
        # if the break is not on then it will run the code
        # this part put the coordinates in and check if the coordinates are safe or dangerous
        if not bool_break:
            if user_direction[move] == 'd':
                move_down(user_units[move])
                if bool_break:
                    break
            elif user_direction[move] == 'r':
                move_right(user_units[move])
                if bool_break:
                    break
            elif user_direction[move] == 'l':
                move_left(user_units[move])
                if bool_break:
                    break
            elif user_direction[move] == 'u':
                move_up(user_units[move])
                if bool_break:
                    break
        # This increase the move counter by 1
        move += 1

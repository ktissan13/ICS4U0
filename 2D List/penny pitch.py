# Penny Pitch
# Tissan Kugathas
# ICS4U0
# September 13 2019

# imports random library
import random 

# This list represent the box where the player has the coin in
chart = []
# This list contains all the game prizes 
prizes = ['PUZZLE','GAME','BALL','POSTER','DOLL']
# These Variables keep count the amount of prizes toggled
puzzle_count = 0
game_count = 0
ball_count = 0
poster_count = 0
doll_count = 0

# This for loop creates the chart/Board for the game
for colum in range(5):
    # makes the colum
    chart.append([])
    for row in range(5):
        # make the row
        chart[colum].append([])
        
# This for loop puts the prizes in random spots on the chart/board
# It will run until there are three of each prizes on the chart/board
for prize in prizes:
    # This is a bool to run the while loop
    loop = True 
    while loop:
        # counter is set to zero
        # this counter runs until it finds three of the current prize is on the board
        count = 0
        # This gets a random colum for the prize
        colum = random.randint(0,4)
        # This gets a random row for the prize
        row = random.randint(0,4)
        # If the random coordinates for the prize does not have a prize in it already, then it will place the prize
        if chart[colum][row] == []:
            # puts the prize in the spot
            chart[colum][row] = prize
        # This checks if the three of the current prize is on the board
        for colum in range(len(chart)):
            # counts how many there are
            count += chart[colum].count(prize)
        # if there is 3 of the current prize then stop the loop and go to the next prize
        if count == 3:
            loop = False
        
# This print the chart/board of the game
for colum in chart:
    print(colum)
print()

# This loop is to place the pennies in random places
for pennies in range(10):
    # gets a random colum for the penny
    colum = random.randint(0,4)
    # gets a random row for the penny
    row = random.randint(0,4)
    # if the coordinates of the penny is on a prize then the counter for that prize will go up by one
    if chart[colum][row] == 'PUZZLE':
        puzzle_count += 1
    elif chart[colum][row] == 'GAME':
        game_count += 1
    elif chart[colum][row] == 'BALL':
        ball_count += 1
    elif chart[colum][row] == 'POSTER':
        poster_count += 1
    elif chart[colum][row] == 'DOLL':
        doll_count += 1
        
# if the penny hits one of the prize three times, it will tell the user the prize they got
# if they did not win anything, it will tell them that they didn't win anything 
if puzzle_count == 3:
    print('Congrats, you won a puzzle!')
elif game_count == 3:
    print('Congrats, you won a game!')
elif ball_count == 3:
    print('Congrats, you won a ball!')
elif poster_count == 3:
    print('Congrats, you won a poster!')
elif doll_count == 3:
    print('Congrats, you won a doll!')
else:
    print("Sorry you didn't win anything")
    

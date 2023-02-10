import random



# This class Ship provides the attributes and methods for the  game. As method it has print_board function (which prints the board according to the 8x8 board and coordinates given) 
# get_ship_location(Asks for the coordinates and save them in  row, column variables if it matches the specifications) create_ships (generates random coordinates) 
# count_hit_ships (keeps track of the score) and Game( which calls all the functions to play the game) and as attributes it takes Hidden_Pattern (saves coordinates where the ship is located) and Guess_Pattern ( which saves coordinates guessed by the user)



class Ship:

    def __init__(self,Hidden_Pattern=None,Guess_Pattern=None):
            self.Hidden_Pattern = Hidden_Pattern
            self.Guess_Pattern = Guess_Pattern



    def print_board(self):
        print('  1 2 3 4 5 6 7 8')
        row_num=1
        for row in self.Guess_Pattern:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num +=1

    #Get coordinates from the user
    def get_ship_location(self):
        
        column=input('Pick your x-coordinate from 1 to 8 ') #Asks for the coordinates and save them in a  column variable if it matches the specifications
        while column not in '12345678':
            print("Please enter a valid column ")
            column=input('Please enter a ship column from 1 to 8 ')
        row=input('Pick your y-coordinate from 1 to 8 ') #Asks for the coordinates and save them in a row variable if it matches the specifications
        while row not in '12345678':
            print("Please enter a valid coordinate ")
            row=input('Please enter a ship row 1-8 ')
       
        return int(row)-1,int(column)-1

    #Function that creates the ships

    def create_ships(self):  
        
        #for ship in range(2): # Gives the lenght of the ship
        ship_r, ship_cl= random.randint(1,6), random.randint(1,6) #generates random coordinates for the ship.
        print(ship_cl,ship_r)
        i=random.randint(-1, 1)
        j=random.randint(-1, 1)
        self.Hidden_Pattern[ship_r][ship_cl] ='X'
        while i==j or i==(j*(-1)):
            i=random.randint(-1, 1)
            j=random.randint(-1, 1)
        
        self.Hidden_Pattern[ship_r+i][ship_cl+j] = 'X' # replaces the Hidden_Pattern empty space with an X
        

    # Calls the functions to generate the game


    def Game(self):
        self.create_ships()
        print('Welcome to Battleship')
        turns = 5 #Gives amount of attempts for the player to hit
        score=0
        while turns > 0: 
            
            self.print_board()
            row,column =self.get_ship_location()
            if self.Guess_Pattern[row][column] == '-' or self.Guess_Pattern[row][column] == 'X': # Checks if the coordinates given were already selected
                print(' You already guessed that ')

            elif self.Hidden_Pattern[row][column] =='X':
                print(' Congratulations you have hit the battleship ') # Checks if the coordinates of ship localization is the same as the guessed by the user and add a score when hitting or sinking the ship
                self.Guess_Pattern[row][column] = 'X' 
                score=score+1 
                if score == 2: #ends the while loop if user hits the ship twice as they sunk the ship
                    print(' Congratulations you sunk the battleship ')
                    score=5  # set the score 5 if the player sinks it
                    turns = 1
                turns -= 1
            else:
                print(Guess_Pattern[row][column],)
                print('Sorry,You missed')
                self.Guess_Pattern[row][column] = '-' # replaces the Guess_Pattern empty space with a - character
                turns -= 1

            print(' You have ' +str(turns) + ' turns remaining ')
            if turns == 0:
                print('Game Over ')
                break
        print(score)
        return score

Hidden_Pattern=[[' ']*8 for x in range(8)] #creates the board according to the ship coordinates
Guess_Pattern=[[' ']*8 for x in range(8)] #creaates the board according to the coordinates guessed by the user
Ship=Ship(Hidden_Pattern,Guess_Pattern)

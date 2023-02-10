


####Lucia Martinez Torres Code (Only member) 
###Battleship game. It takes two modules called player and battleship, which has the methods to create an save the user and run the game

import player
import battleship


def main():
	
	reg= input('do you want to register? ')#asks the user if they want to register and saves it in a variable
	if reg == 'yes':
		l=player.User.register(player.credentials) #if yes runs the register method in player module
		while l==1:
			l=player.User.register(player.credentials) #if there is a problem runs it again
		
	else:
		print('please log in')
		l = player.User.login(player.credentials)#If the user does not want to register, it starts the login method
		while l != True:
			print('oops something went wrong!, try again')
			l = player.User.login(player.credentials) #Runs the method if the username or password are not found or do not match
		
	print('Welcome ',  player.credentials.userName)
	try:
		score=battleship.Ship.Game()# Initialize game
		player.User.AddScore(player.credentials,score)#Once the game finishes, it runs Addscore method to save the score
	except:
		print('Oooops Something happened! Please start again ')



if __name__ == "__main__":
    main()
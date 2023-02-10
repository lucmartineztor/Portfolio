import json


# This module, tha Class User, provides the attributes and methods for the user.  As method it has register function (which saves the user with they password) 
# login(checks if the user exists and if the password given by the user is the same as registerd) and Addscore (which saves the score obtanined 
# by the player) and its attributes are userName, userPassword and score.

class User:   

	#attributes userName, userPassword and score are initialized 

	def __init__(self,userName=None,userPassword=None,Score=None):
		self.userName = userName
		self.userPassword = userPassword
		self.Score = Score

	#Creates (if doesn't exist already) a text file to save the player's userName and userPassword if it's not already saved. If it is, it prints a warning sign that it already exists.
	#Documents are saved as dictionaries (json)

	def register(self):
		import json
		l=0
		credentials.userName = input("Enter Your Name: ") #asks the user for their Name and Password
		credentials.userPassword = input("Enter Your Password: ")
		user=[{'Name':credentials.userName,'Password': credentials.userPassword}] #generates a tuple with the user's Name and Password
		

		try:
			
			with open('myfile.txt') as file: # opens the file and checks every document
				ListOfElements=json.load(file)
			for i in range(len(ListOfElements)):

				if ListOfElements[i]['Name']== credentials.userName and ListOfElements[i]['Password']== credentials.userPassword:#Compares if The password and username is already in file
					print('Sorry, you are already registered')# if data is found in file, prints it is already registered
					l=1
					return l
					

			
			if l==0:
				
				ListOfElements.append(user[0]) #else, it saves the new user Name and password
				file.close()
				file= open("myfile.txt","w")
				json.dump(ListOfElements,file)
				l=0
				return l
				

			
			
		except:
			
			file= open("myfile.txt","w") # In case file doesn't exist, it crates the file and adds the username and password
			user=json.dump(user,file)
			return l
			
			
	def login(self):

		#Checks if the userName and password is already registered (if it is already saved in the file as a document)
		try:
			self.userName = input("Enter Your Name: ")#asks the user for their Name and Password
			self.userPassword = input("Enter Your Password: ") 
			user=[{'Name': self.userName,'Password': self.userPassword}]#generates a tuple with the user's Name and Password
			with open('myfile.txt') as file: # opens the file and checks every document
					ListOfElements=json.load(file)
					
		 
			for i in range(len(ListOfElements)):
				
				if ListOfElements[i]['Name']== self.userName and ListOfElements[i]['Password']==self.userPassword: #Compares if The password and username is already in file
					print('user logged')
					return True #returns True if it finds the document with same name
				else:
					pass
				
		except:
			print('User Not logged')
			return False
	
	def AddScore(self,score):

		#Saves the score obtained by the user

		self.score=score
		try:
			with open('myfile.txt') as file: # opens the file  and search for the document with the userName and password given
					ListOfElements=json.load(file)
			for i in range(len(ListOfElements)):
				if ListOfElements[i]['Name']==self.userName and ListOfElements[i]['Password']==self.userPassword:
					ListOfElements[i]['score']=self.score	#adds a field Score to it and adds the score obtained
			file.close()
			file= open("myfile.txt","w")
			json.dump(ListOfElements,file) #saves the new field to the file
		except Exception as e:
			print ('Score was not saved')




credentials=User()

#newUser=User.register(credentials)
#olduser=User.login(credentials)
#User.AddScore(credentials,3)

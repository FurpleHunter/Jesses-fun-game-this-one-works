import random
import time
ComputerPoints=1
steal=0
Points=1
Tutorial=(input("Type yes to learn how to play, type somthing else to skip:"))
if Tutorial==("yes"):
	print ("")
	print("You choose a number, and the computer chooses a number. Everyone starts off with 1 point. Player starts off with 0 steals(Which can be bought from shop(a power-up)). If you get the same number you kill the computer and you get 1 point. If you both get different numbers the computer gets a point. You can only choose numbers from 1-5. If Computer gets 0 points YOU WIN if computer gets 5 points he wins! Hard eh? Are you brave enough? When PC gets 0 points you win! You will get the hang of it :)")
	print ("")
	print ("Changing in 30 seconds...")
	time.sleep(25)
	print ("5...")
	time.sleep(1)
	print ("4...")
	time.sleep(1)
	print ("3...")
	time.sleep(1)
	print ("2...")
	time.sleep(1)
	print ("1...")
	for i in range(0,100):
		print ("")
if Tutorial!=("yes"):
	for i in range(0,10):
		ComputerText=random.randint(1,4)
		if ComputerPoints==0:
			for i in range(0,10000):
				print("GAME OVER YOU WIN")
		if ComputerPoints==5:
			for i in range(0,1000):
				print("YOU LOOSE")
		for i in range(0,100):
			print ("")
		if ComputerText==4:
			print  ("                                                             *CHAT*")                   
			print ("Computer> I actually don't like progrmming.")
			time.sleep(5)
			print ("Computer> Programming*. I actually made this game :P. The iroy.")
			time.sleep(7)
			print ("Computer> irony*. You are a cool guy, i will give you one point :).                             +1 POINTS")
			Points=Points+1
			time.sleep(5)
		if ComputerText==3:
			print  ("                                                             *CHAT*")                   
			print ("Computer> You have ", Points, " Points... Uhm pretty good :)")
			time.sleep(3)
			print ("Computer> Do you play LoL?")
			time.sleep(4)
			print ("Computer> Eh... LoL is for nerds...a")
			time.sleep(2)
		if ComputerText==2:
			print  ("                                                             *CHAT*")                   
			print ("Computer> Uhm... Since i am an Acer computer. Is my parents Acer?!")
			time.sleep(3)
			print ("Computer> Yeah om lonly")
			time.sleep(3)
			print ("Computer> I could be watching NetFlix")
			time.sleep(3)
		if ComputerText==1:
			print  ("                                                             *CHAT*")                   
			print ("Computer> I have ", ComputerPoints, " Points... Not bad")
			time.sleep(5)
			print ("Computer> K lets play now")
			time.sleep(7)
			print ("Computer> Oops sorry i was checking my texts, choose a number now")
			time.sleep(5)
		for i in range(0,100):
			print ("")
		print ("                                                                      *SHOP*   You have ", Points, " Points")
		print ("Items in stock: steal(Makes PC feel bad) (Costs: 2 Points)")
		Shop=(input("What do you want to BUY?:"))
		if Shop==("steal") and Points<2:
			print ("You don't have enough points you theif!")
		if Shop==("steal") and Points>=2:
			print ("")
			print ("Points-2")
			print ("steal+1")
			print("STEAL BOUGHT!")
			print ("")
			steal=steal+1
			Points=Points-2
		if Shop!=("steal"):
			print ("You bought nothing")
		time.sleep(3)
		for i in range(0,100):
			print ("")
		print ("                                                             You have ", Points, " Points")
		print ("                                                             Computer has ", ComputerPoints, " Points")
		print("")
		PlayerNum=int(input("Choose your number:"))
		print ("                                                             You have ", steal, " steal power-ups")
		Power=input("Powers?")
		if Power==("steal") and steal>=1:
			for i in range(0,100):
				print ("")
			print (" ########## KILL POWER UP USED ########## (EPIC MUSIC)")
			time.sleep(3)
			print ("__________")
			print ("*COMPUTER INSTA-KILLED*")
			print ("                                             +1 POINT")
			print ("                                             COMPUTER -1 POINT")
			print ("                                             POINT STOLEN!")
			print ("Computer> WHY U DO DIS :'( you make me cry. You must really hate me :(")
			print ("__________")
			Points=Points+1
			ComputerPoints=ComputerPoints-1
			steal=steal-1
			time.sleep(6)
		if PlayerNum>6:
			for i in range(0,100):
				print ("")
			print ("______________________")
			print ("YOUR NUMBER MUST BE EQUAL TO OR SMALLER THAN 6")
			print ("______________________")
			time.sleep(2)
			for i in range(0,100):
				print ("")			
		else:
			ComputerNum=random.randint(1,6)
			for i in range(0,100):
				print("")
			print ("______________________")
			print ("")
			print ("Your number is")
			print (PlayerNum)
			print ("Computer's number is")
			print (ComputerNum)
			if PlayerNum==ComputerNum:
				print ("")
				print ("*COMPUTER KILLED*")
				print ("                                                             +1 POINTS")
				Points=Points+1
			else:
				print ("*COMPUTER SURVIVED*                                        COMPUTER GOT 1 POINT")
				ComputerPoints=ComputerPoints+1
			time.sleep(7)
			print ("______________________")
			for i in range(0,100):
				print ("")	
		
from IPython.display import clear_output
# clear_output()
#main variables
board_dict_default = {1:" 1 ",2:"|",3:" 2 ",4:"|",5:" 3 ",6:"\n",7:"---",8:"+",9:"---",10:"+",11:"---",12:"\n",
                  13:" 4 ",14:"|",15:" 5 ",16:"|",17:" 6 ",18:"\n",19:"---",20:"+",21:"---",22:"+",23:"---",24:"\n",
                 25:" 7 ",26:"|",27:" 8 ",28:"|",29:" 9 "}

board_dict = {1:" 1 ",2:"|",3:" 2 ",4:"|",5:" 3 ",6:"\n",7:"---",8:"+",9:"---",10:"+",11:"---",12:"\n",
                  13:" 4 ",14:"|",15:" 5 ",16:"|",17:" 6 ",18:"\n",19:"---",20:"+",21:"---",22:"+",23:"---",24:"\n",
                 25:" 7 ",26:"|",27:" 8 ",28:"|",29:" 9 "}

board_placeholders = {1:1,2:3,3:5,4:13,5:15,6:17,7:25,8:27,9:29}

available_placeholders = []

winning_combinations = [(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,8),(1,4,3),(2,5,8),(3,6,9)]


user1_inputs = []
user2_inputs = []

user1 = "User 1"
user2 = "User 2"

place_2 = "0"
place_1 = "0"

def paste_on_board(n,letter):
    for place,value in board_dict.items():
        if(place == n):
            board_dict.update({place:" {} ".format(letter)})
    return 0

def print_board():
    printable_data = ""
    for place,value in board_dict.items():
            if(place in (1,7,13,19,25)):
            	printable_data = printable_data + "*****   " + value 
            elif(place in (5,11,17,23,29)):
            	printable_data = printable_data + value + "   *****"
            else:
            	printable_data += value

    print("***************************")
    print("***************************")
    print("***************************")
    print("*****                 *****")
    print(printable_data)
    print("*****                 *****")
    print("***************************")
    print("***************************")
    return 0

def reduce_available_placeholder(n):
	if n in available_placeholders:
		available_placeholders.remove(n)
		return True
	else:
		return False
	return False

def is_winner(v):
	who_is_winner = v
	for a,b,c in winning_combinations:
		if a in user1_inputs and b in user1_inputs and c in user1_inputs:
			who_is_winner = 1
			break
		if a in user2_inputs and b in user2_inputs and c in user2_inputs:
			who_is_winner = 2
			break
	return who_is_winner

def check_input(val):
	if(val.isdigit() == True and (int(val) in available_placeholders)):
		return True
	else:
		return False
	return False


def user_input(user_flag,user):
	val = "asdf"
	if(user_flag == 0 and not (not available_placeholders)):
		while check_input(val) == False:
			val = input('{} : Where do you need X ?{}'.format(user,available_placeholders))
			if(check_input(val) == False):
				clear_output()
				print("Please enter only available choices among {}".format(available_placeholders))
		else:
			user1_inputs.append(int(val))
			reduce_available_placeholder(int(val))
			paste_on_board(board_placeholders.get(int(val)),"X")
			return True
	if(user_flag == 1 and not (not available_placeholders)):
		while check_input(val) == False:
			val = input('{} : Where do you need O ?{}'.format(user,available_placeholders))
			if(check_input(val) == False):
				clear_output()
				print("Please enter only available choices among {}".format(available_placeholders))
		else:
			user2_inputs.append(int(val))
			reduce_available_placeholder(int(val))
			paste_on_board(board_placeholders.get(int(val)),"O")
			return True
	return False



def game_on():
	flag = 0
	while is_winner(3) == 3:
		if(flag == 0 and (user_input(0, user1) == True)):
			clear_output()
			print_board()
			flag = 1
		elif(flag == 1 and (user_input(1, user2) == True)):
			clear_output()
			print_board()
			flag = 0
	else:
	# 	print("{} inputs : {}".format(user1,user1_inputs))
	# 	print("{} inputs : {}".format(user2,user2_inputs))
	# 	print(is_winner())
		if(is_winner(3) == 1):
			print("********************************************")
			print("**                                        **")
			print("       Congratulations {}, You won !!       ".format(user1))
			print("**                                        **")
			print("********************************************")
		if(is_winner(3) == 2):
			print("********************************************")
			print("**                                        **")
			print("       Congratulations {}, You won !!       ".format(user2))
			print("**                                        **")
			print("********************************************")
	return 0

print("Welcome to Tic Tac Toe......\n")
user1 = input("Please enter First User Name : ")
user2 = input("Please enter Second User Name : ")

ready_flag = "y"
while ready_flag == "y":
	user1_inputs = []
	user2_inputs = []
	available_placeholders = []
	board_dict = {}
	board_dict = board_dict_default
	for i in range(1,10,1):
		available_placeholders.append(i)
	result = game_on()
	print_board()
	if(result == 0):
		ready_flag = input("You want to play again ? y/n - ")
		if(ready_flag == "n" or ready_flag == "N"):
			print_board()
			continue
else:
	print_board()
	if(is_winner(3) == 1):
		print("********************************************")
		print("**                                        **")
		print("       Last Winner is {}.       ".format(user1))
		print("**                                        **")
		print("********************************************")
	if(is_winner(3) == 2):
		print("********************************************")
		print("**                                        **")
		print("       Last winner is {}.       ".format(user2))
		print("**                                        **")
		print("********************************************")





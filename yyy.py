game = np.full((3,3)," ").astype('object')

win = False



def board():
    dashes = ' ---'
    pipe = '|'
    line= dashes * 3

    print(line)
    print(pipe , game[0][0] , pipe , game[0][1] , pipe , game[0][2] , pipe)
    print(line)
    print(pipe , game[1][0] , pipe , game[1][1] , pipe , game[1][2] , pipe)
    print(line)
    print(pipe , game[2][0] , pipe , game[2][1] , pipe , game[2][2] , pipe)
    print(line)


def player_1():
    global win
    while win != True :
        move = input(' player_1, take your move (in the format row,col) :')
        move = move.strip()
        move = move.split(",")
        row = int(move[0])
        col = int(move[1])
        position = game[row - 1][col - 1]
        if position == " " :
            game[row - 1][col - 1] = 'X'
            break
        else :
            print('wrong input ! please try again .')



def player_2():
    global win
    while  win != True :
        move = input(' player_2, take your move (in the format row,col) :')
        move = move.strip()
        move = move.split(",")
        row = int(move[0])
        col = int(move[1])
        position = game[row - 1][col - 1]
        if position == " ":
            game[row - 1][col - 1] = 'O'
            break
        else:
            print('wrong input ! please try again .')


def check_winner():
	global win
	for i in range(3):
		# columns
		if game[0][i] == game[1][i] == game[2][i]:
			if game[0][i] == 'X':
				print('player 1 WINS !')
				win = True
			elif game[0][i] == 'O':
				print('player 2 WINS !')
				win = True

		# rows
		elif game[i][0] == game[i][1] == game[i][2]:
			if game[i][0] == 'X':
				print('player 1 WINS !')
				win = True
			elif game[i][0] == 'O':
				print('player 2 WINS !')
				win = True

	# diagnols
	if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0]:
		if game[1][1] == 'X':
			print('player 1 WINS !')
			win = True
		elif game[1][1] == 'O':
			print('player 2 WINS !')
			win = True

def Game():
    full=0
    while full < 9 and win != True :
        player_1()
        board()
        check_winner()
        player_2()
        board()
        check_winner()

        full+=1

while True:
    Game()
    c = input("would you like to play again ? ")
    if c == 'yes' :
        Game()
    else:
        break
def start():
    global a
    a = input('Welcome to the Game Emporium! Which game would you like to play? [Rock Paper Scissors|Tic Tac Toe|Sticks]\n>')
    if (a == 'Rock Paper Scissors'):
        print('Initializing...')
        rpsrun()
    elif (a == 'rock paper scissors'):
        print('Initializing...')
        rpsrun()
    elif (a == 'rps'):
        print('Initializing...')
        rpsrun()
    elif (a == 'Tic Tac Toe'):
        print('Initializing...')
        tttrun()
    elif (a == 'tic tac toe'):
        print('Initializing...')
        tttrun()
    elif (a == 'ttt'):
        print('Initializing...')
        tttrun()
    elif (a == 'Sticks'):
        print('Initializing...')
        sticksrun()
    elif (a == 'sticks'):
        print('Initializing...')
        sticksrun()
    elif (a == 's'):
        print('Initializing...')
        sticksrun()

def tttrun():

    import random

    board_dic = {'1': ' ', '2': ' ', '3': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '7': ' ', '8': ' ', '9': ' '}


    def board_display(board):
        print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
        print('- + - + -')
        print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
        print('- + - + -')
        print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])


    def check_winner(player):
        win_txt = f'\nPlayer {player} won 👏👏👏\nGame Over!'
        if board_dic['1'] == board_dic['2'] == board_dic['3'] != ' ':
            print(win_txt)
            return True
        elif board_dic['4'] == board_dic['5'] == board_dic['6'] != ' ':
            print(win_txt)
            return True
        elif board_dic['7'] == board_dic['8'] == board_dic['9'] != ' ':
            print(win_txt)
            return True
        elif board_dic['1'] == board_dic['4'] == board_dic['7'] != ' ':
            print(win_txt)
            return True
        elif board_dic['2'] == board_dic['5'] == board_dic['8'] != ' ':
            print(win_txt)
            return True
        elif board_dic['3'] == board_dic['6'] == board_dic['9'] != ' ':
            print(win_txt)
            return True
        elif board_dic['1'] == board_dic['5'] == board_dic['9'] != ' ':
            print(win_txt)
            return True
        elif board_dic['3'] == board_dic['5'] == board_dic['7'] != ' ':
            print(win_txt)
            return True


    def first_player():
        return random.randint(1, 2)


    def swap_players(player):
        if player == 'O':
            return 'X'
        else:
            return 'O'


    def play_game():
        num_of_moves = 0
        all_players_input = []
        game_over = False

        if first_player() == 1:
            player = 'X'
        else:
            player = 'O'

        while not game_over:
            player_input = input(f'\nPlayer_{player}: ')
            if player_input in all_players_input:
                print('This cell is busy, try another one.')
                continue
            elif player_input not in board_dic.keys():
                print('Only numbers from 1 to 9 allowed. Please try again.')
                continue
            num_of_moves += 1
            all_players_input.append(player_input)
            board_dic[player_input] = player
            board_display(board_dic)
            if check_winner(player):
                game_over = True

            if num_of_moves == 9 and not check_winner(player):
                print('Game Draw! 🙃')
                game_over = True
            player = swap_players(player)


    while input("\nDo you want to play a game of TiTacToe? Type 'y' or 'n': ") == "y":
        for key in board_dic.keys():
            board_dic[key] = ' '
        play_game()
    else:
        start()

def rpsrun():

    computerscore = 0
    userscore = 0
    numgames = int(input("Welcome to rock, paper, scissors.\nHow many games would you like to play?\n"))
    userinput = ""
    computerchoice = ""
    userwin = False
    draw = False
    choice = ""

    for x in range(0, numgames):
        import random
        generatednum = random.randint(1,3)
        if generatednum == 1:
            computerchoice = "rock"
        elif generatednum == 2:
            computerchoice = "paper"
        elif generatednum == 3:
            computerchoice = "scissors"

        userinput = input("Select rock, paper, or scissors\n")

        if userinput == "rock" and computerchoice == "scissors":
            print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
            userscore += 1
        elif userinput == "rock" and computerchoice == "paper":
            print("You selected",userinput,"and the computer selected",computerchoice,"You lost this round!")
            computerscore += 1
        elif userinput == "r" and computerchoice == "scissors":
            print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
            userscore += 1
        elif userinput == "r" and computerchoice == "paper":
            print("You selected",userinput,"and the computer selected",computerchoice,"You lost this round!")
            computerscore += 1
        if userinput == "paper" and computerchoice == "rock":
            print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
            userscore += 1
        elif userinput == "paper" and computerchoice == "scissors":
            print("You selected",userinput,"and the computer selected",computerchoice,". You lost this round!")
            computerscore += 1
        elif userinput == "p" and computerchoice == "rock":
            print("You selected",userinput,"and the computer selected",computerchoice,". You won this round!")
            userscore += 1
        elif userinput == "p" and computerchoice == "scissors":
            print("You selected",userinput,"and the computer selected",computerchoice,". You lost this round!")
            computerscore += 1
        if userinput == "scissors" and computerchoice == "paper":
            print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
            userscore += 1
        elif userinput == "scissors" and computerchoice == "rock":
            print("You selected",userinput,"and the computer selected",computerchoice,"You lost this round!")
            computerscore += 1
        elif userinput == "s" and computerchoice == "paper":
            print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
            userscore += 1
        elif userinput == "s" and computerchoice == "rock":
            print("You selected",userinput,"and the computer selected",computerchoice,"You lost this round!")
            computerscore += 1

    if userscore > computerscore:
        userwin = True
    elif userscore == computerscore:
        draw = True

    if userwin == True:
        print("Congratulations, you won!\nYour score:",userscore,"\nComputer's score:",computerscore)
    elif draw == True:
        print("You drew!\nYour score:",userscore,"\nComputer's score:",computerscore)
    elif userwin == False:
        print("I'm sorry, but you lost.\nYour score:",userscore,"\nComputer's score:",computerscore)

    choice = str(input("Would you like to play again? y/n\n"))
    if choice == "y":
        rpsrun()
    if choice == 'n':
        start()

def sticksrun():
    import random

    def main():
       # Global Variables
      active = True
      is_player1_turn = True
      is_computer = False
      player1_score = 0
      player2_score = 0
      player2_title = "Player 2"
      entries = 20
      valid_options = [["A", "a", "B", "b", "C", "c"], [1, 2, 3]]


      def validate_input (valid_options_index, option):
        """
        Validates Inputted Answers
        :param valid_options_index: Determines which set is used for comparison
        :param option: Incoming option
        :return: Validated option
        """
        validate = True
        while(validate):
          validate = True if option not in valid_options[valid_options_index] else False
          if(validate):
            option = input("Invalid: Please select one of the options above: ")
        return option

      def print_board (rows, entries):
        """
        Prints the board of sticks
        :param rows: Number of rows
        :param entries: Number of bar entries in each row
        """
        for row in range(rows):
          entry = "| " * entries
          print(entry)

      """
      Starts the Sticks Game
      """
      # Start of Game
      print(
        '''
      -------------------------------------------
         _     _     _     _     _     _
        / \   / \   / \   / \   / \   / \\
       ( S ) ( t ) ( i ) ( c ) ( k ) ( s )
        \_/   \_/   \_/   \_/   \_/   \_/
      -------------------------------------------
      \nInstructions:
        • During every turn, a player can take one, two, or
          three sticks from the board.
        • The player who takes the last stick, loses
        '''
      )

      # Handles Two Player and Computer Options
      print(
      """
      ****************  MENU   *****************
      \ta) Two Player          b) Computer
      """
      )
      player_choice = input("\nEnter a or b: ")
      validated_choice = validate_input(0, player_choice)

      # Handle computer verses player 2 options
      if(validated_choice in ["B", "b"]):
        is_computer = True
        player2_title = "Computer"
      elif(validated_choice in ["A", "a"]):
        is_computer = False
        player2_title = "Player 2"


      while(active):
        # Display Score
        print(
          """
                  CURRENT SCORE
          --------------------------------
          Player 1: %(p1_sticks)d     %(player2)s: %(p2_sticks)d
          """%{"player2": player2_title, "p1_sticks": player1_score, "p2_sticks": player2_score }
        )

        # Print board
        print_board(5, entries)
        # Keep Track of Turns
        print("\n\t\t\tPlayer 1's Turn") if is_player1_turn else print("\n\t\t\t%s's Turn"%(player2_title))

        # Handle each play
        play = 0
        if(is_computer and not is_player1_turn):
          play = random.randint(1,3)
          player2_score += play
        else:
          initial_play = int(input("\nEnter 1, 2 or 3: "))
          play = validate_input(1, initial_play)

          if(is_player1_turn):
            player1_score += play
          else:
            player2_score += play;

        # Handle end game condition
        if(player1_score + player2_score >= 20):
          active = False
          print("\n\t\t\t%s Wins!"%(player2_title)) if is_player1_turn else print("\n\t\t\tPlayer 1 Wins!")

        is_player1_turn = not is_player1_turn
        entries -= play

    if __name__ == '__main__':
      main()

start()

from win_conditions import WinConditions
from rules_art import rules_art
import os

class Game:
    def __init__(self) -> None:
        self.round_count = 0
        self.max_rounds = 0
        self.mode = 0
        self.Win_Condition = WinConditions()
        self.run_game()


# Runs the gameplay loop sequence until the player decides they are done playing.
    def run_game(self):
        game_continue = "1"
        while game_continue == "1":
            os.system('cls')  #Attempt at clearing the terminal after each game. WIP
            self.display_rules()
            self.game_mode()
            self.generate_players()
            self.round_count_option()
            self.start_round()
            self.display_winner()
            game_continue = input("Would you like to play again? Please enter - 1: Yes or 2: No\n")

# prints the game rules in a clean and graphical way.
    def display_rules(self):
        print(rules_art)

# calls the method to create the game's players
    def generate_players (self):
        self.Win_Condition.player_list.create_player(self.mode)

# Allows the player to select between single player and multiplayer. 
    def game_mode(self):
        self.mode = int(input('''\n
Select a game mode:
1 - Single Player 
2 - Multiplayer
Please select your game mode! 1 or 2:\n'''))
        return self.mode

# Allows the player to decide how many round they would like to player and then determines the number of wins needed.
    def round_count_option(self):
        self.round_count = int(input("Enter the number of rounds you'd like to play:\n"))
        self.Win_Condition.how_many_wins(self.round_count)

# After the user has decided all the game mode choices, this will begin the game rounds till the win condition is met.
    def start_round(self):
        game_over = False
        self.Win_Condition.how_many_wins(self.round_count)
        current_round = 1
        while not game_over:
            print("___________________________________________________________")
            print(f"ROUND: {current_round}/{self.round_count}")
            self.gesture_selection()
            self.round_result()
            self.display_score()
            current_round += 1
            game_over = self.Win_Condition.win_condition_check()

# Calls the gesture selection method for all players in the game.
    def gesture_selection(self):
        for players in self.Win_Condition.player_list.players:
            players.pick_gesture()

# Determins who won the round increasing their score and then displays it to the players.
    def round_result(self):
        player_one_result = self.Win_Condition.gesture_comparison(self.Win_Condition.player_list.players[0],self.Win_Condition.player_list.players[1])
        if player_one_result:
            self.Win_Condition.player_list.players[0].score += 1
            print(f"\nPlayer One's {self.Win_Condition.player_list.players[0].choice} beats Player Two's {self.Win_Condition.player_list.players[1].choice} this round! \n")
        elif player_one_result == False:
            self.Win_Condition.player_list.players[1].score += 1
            print(f"\nPlayer Two's {self.Win_Condition.player_list.players[1].choice} beats Player One's {self.Win_Condition.player_list.players[0].choice} this round! \n")
        else:
            print("\nThis round is a draw! \n")   

# Displays the current score of both players.
    def display_score(self):
        print(f"Player One score: {self.Win_Condition.player_list.players[0].score}/{self.Win_Condition.wins_needed} | "\
        f"Player Two score: {self.Win_Condition.player_list.players[1].score}/{self.Win_Condition.wins_needed}!\n")

# Displays the winner of the game.
    def display_winner(self):
        if self.Win_Condition.player_list.players[0].score > self.Win_Condition.player_list.players[1].score:
            print("Player One is the Winner!\n")
        if self.Win_Condition.player_list.players[1].score > self.Win_Condition.player_list.players[0].score:
            print("Player Two is the Winner!\n")
from Ai import Ai
from players import Player


class PlayerList:
    def __init__(self):
        self.players = []


# Based off of the player's mode choice will create either two players or a player and an ai for the game.
    def create_player(self, mode):
        if mode == 1:
         player_one = Player("Player One")
         player_ai = Ai("Player Two")
         self.players = [player_one, player_ai]
        
        elif mode == 2:
         player_one = Player("Player One")
         player_two = Player("Player Two")
         self.players = [player_one, player_two]
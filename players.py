

class Player:
    def __init__ (self, name):
        self.name = name
        self.score = 0
        self.gestures = ("rock", "paper", "scissors", "lizard", "spock")
        self.choice = ""


# Allows the player to pick a gesture from a list for their turn.
    def pick_gesture(self):
        invalid = True
        while invalid:
            print(f"\nRock | Paper | Scissors | Lizard | Spock\n")
            self.choice = input(f'{self.name} please pick a gesture:\n').lower()
            if self.gesture_validation():
                invalid = False
                return self.choice

# Takes in the player's gesture shoice and makes sure it is a valid gesture.
    def gesture_validation(self):
        if self.choice in self.gestures:
            return True
        else:
            return False   
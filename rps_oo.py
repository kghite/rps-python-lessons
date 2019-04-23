"""
Multi-agent Rock Paper Scissors Game
Last player standing rules

Learning Goal:
    * Using classes to structure control

Practiced Concepts:
    * Functions
    * List comprehensions
"""

import random

"""
Rock paper scissors player
"""
class RPSPlayer:

    def __init__(self, player_name):
        self.name = player_name
        self.plays = ['rock', 'paper', 'scissors']
        self.playing = True

        self.play = None

    """
    Randomly choose a play
    """
    def get_play(self):
        self.play = random.choice(self.plays)


"""
Rock paper scissors game control
"""
class RPSGame:
    
    def __init__(self): 
        self.players = None
        self.gameover = False
        self.player_names = []

    """
    Check if a player lost a round
    Returns: boolean lost value
    """
    def check_player(self, p1):
        for p2 in self.players:
            # Look for loss
            if p1.play == 'rock':
                if p2.play == 'paper':
                    return True
            elif p1.play == 'paper':
                if p2.play == 'scissors':
                    return True
            elif p1.play == 'scissors':
                if p2.play == 'rock':
                    return True
        return False

    """
    Execute one round of the game
    """
    def play_round(self):
        # Update and print the players with new plays
        for player in self.players:
            player.get_play()
            print player.name + ' played ' + player.play

        # Figure out which players lost and remove them
        for player in self.players:
            lost = self.check_player(player)
            if lost:
                print player.name + ' is out of the game.'
                self.players.remove(player)

    """
    Run game rounds until last player standing
    Input: List of player names as strings
    """
    def play_game(self, player_names):
        # Create list of player objects
        self.players = [RPSPlayer(name) for name in player_names]

        # Play rounds until there is only one player left
        round_num = 1
        while len(self.players) > 1:
            print 'Round', round_num
            self.play_round()
            round_num += 1
        
        print self.players[0].name + ' won the game!'



if __name__ == '__main__':
    game = RPSGame()
    game.play_game(['Kara', 'Alex', 'Lena'])
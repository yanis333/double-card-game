from Board import Board
from Player import Player
from AI_Player import AI

class DoubleCardGame:
    _MAX_ROUNDS = 60
    _MAX_CARDS_PER_PLAYER = 12

    def __init__(self, board, players):
        self._board = board
        self._players = players
        self._hasWinner = False

    def playGame(self):
        rounds = 0
        while not self._hasWinner:
            if not rounds < DoubleCardGame._MAX_ROUNDS:
                print('The maximum number of turns ({}) has been reached!\nThe game has ended in a draw.'.format(DoubleCardGame._MAX_ROUNDS))
                break
 
            self._playRound()
            rounds += 1

    def getPlayers(self):
        return self._players

    def _playRound(self):
        for player in self._players:
            player.takeTurn()
            self._board.printBoard()
            print()
            if self._board.hasWinner():
                self._hasWinner = True 

                winning_markers = self._board.getWinningMarkers()
                player1, player2 = self._players

                # case 1: two winners, winner is the person who last played
                # case 2: 1 winner, winner is the person whos marker corresponds to the winning marker

                if len(winning_markers) == 2:
                    print('{} won!'.format(player.getName()))
                elif len(winning_markers) == 1:
                    if player1.getMarker() == winning_markers[0]:
                        print('{} won!'.format(player1.getName()))
                    else:
                        print('{} won!'.format(player2.getName()))

                break

if __name__ == '__main__':
    print('Let\'s play DoubleCardGame!\n')
        
    mode = input('Select the game mode:\n    1 - Human vs. Human\n    2 - Human vs. AI\n')
        
    player1_name = input('\nEnter player 1\'s name: ')
    player1_marker = input('\nSelect player 1\'s marker:\n1 - Dots \n2 - Color\n')
    player2_marker = None

    if int(player1_marker) == 1:
        player1_marker = Player.Marker.DOTS
        player2_marker = Player.Marker.COLOR
    elif int(player1_marker) == 2:
        player1_marker = Player.Marker.COLOR
        player2_marker = Player.Marker.DOTS
    
    if int(mode) == 1:
        player2_name = input('\nEnter player 2\'s name: \n')
    else: 
        player2_name = '** NORA FAKOTAKIS **'

    board = Board(DoubleCardGame._MAX_CARDS_PER_PLAYER * 2)

    player1 = Player(player1_name, player1_marker, board, DoubleCardGame._MAX_CARDS_PER_PLAYER)
    
    player2 = None
    if int(mode) == 2:
        ai_type = input('\nSelect the AI type:\n1 - Regular \n2 - Tourney\n')
        
        isTraceFile = input('\nDo you want a trace file:\n1 - Yes \n2 - No\n')

        if int(ai_type) == 1:
            ai_type = 'REGULAR'
        elif int(ai_type) == 2:
            ai_type = 'TOURNEY'

        if int(isTraceFile)==1:
            isTraceFile =True
        else:
            isTraceFile =False

        player2 = AI(player2_name, player2_marker, board, DoubleCardGame._MAX_CARDS_PER_PLAYER,isTraceFile, ai_type)
    else:
        player2 = Player(player2_name, player2_marker, board, DoubleCardGame._MAX_CARDS_PER_PLAYER)
    
    first = input('\nWho goes first?:\n    1 - {}\n    2 - {}\n'.format(player1_name, player2_name))

    if int(first) == 1:
        players = [player1, player2]
    else:
        players = [player2, player1]


    print()
    game = DoubleCardGame(board, players)

    game.playGame()

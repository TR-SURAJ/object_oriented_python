class Player:
 
    def __init__(self, x, y):
        self.x = x
        self.y = y

player1 = Player(5, 6)
player2 = Player(2, 4)
player3 = Player(3, 6)

players = [player1, player2, player3]

for player in players:
    print(f"X: {player.x} Y: {player.y}")
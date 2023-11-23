class Player:
 
    def __init__(self, x, y):
        self.x = x
        self.y = y


player = Player(6, 8)
print(player.x)
print(player.y)

attributes = ['x', 'y'] 

for attribute in attributes:
    delattr(player, attribute)

print(player.x)
print(player.y)
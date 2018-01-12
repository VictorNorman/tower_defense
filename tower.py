
class Tower:
    '''Represents a tower that can be placed on the board, and attacks invaders.'''

    def __init__(self, x, y):
        '''x and y are the location of this tower in the grid of cells.'''
        self._x = x
        self._y = y
        self.shootBehavior = None
        self._cost = 0
        self._range = 75
        self._reloadTime = 0
        self._projectile = None

    def get_range(self):
        return self._range

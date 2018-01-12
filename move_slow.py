
from interface import implements
from move_behavior import MoveBehavior

class MoveSlow(implements(MoveBehavior)):

    def move(self, invader):
        """move the invader half the distance of the direction it is going."""
        invader.update_x(invader.get_xdir() / 2)
        invader.update_y(invader.get_ydir() / 2)

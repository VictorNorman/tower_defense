
from interface import implements
from move_behavior import MoveBehavior
import random

class MoveNormal(implements(MoveBehavior)):

    def move(self, invader):
        """move the invader the full distance of the direction it is going."""
        invader.update_x(invader.get_xdir())
        invader.update_y(invader.get_ydir())

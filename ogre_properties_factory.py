from interface import implements
from invader.invader_properties_factory import InvaderPropertiesFactory
from move_normal import MoveNormal


class OgrePropertiesFactory(implements(InvaderPropertiesFactory)):

    def createMoveBehavior(self):
        return MoveNormal()

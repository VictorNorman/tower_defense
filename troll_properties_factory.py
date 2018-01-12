from interface import implements
from invader.invader_properties_factory import InvaderPropertiesFactory
from move_slow import MoveSlow


class TrollPropertiesFactory(implements(InvaderPropertiesFactory)):

    def createMoveBehavior(self):
        return MoveSlow()

from invader.invader_factory import InvaderFactory
from invader.troll_properties_factory import TrollPropertiesFactory
from invader.troll import Troll

class TrollInvaderFactory(InvaderFactory):

    def createInvader(self, canv, invader_path):
        propsFactory = TrollPropertiesFactory()
        return Troll(propsFactory, canv, invader_path)

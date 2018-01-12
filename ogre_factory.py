from invader.invader_factory import InvaderFactory
from invader.ogre_properties_factory import OgrePropertiesFactory
from invader.ogre import Ogre


class OgreInvaderFactory(InvaderFactory):

    def createInvader(self, canv, invader_path):
        propsFactory = OgrePropertiesFactory()
        return Ogre(propsFactory, canv, invader_path)

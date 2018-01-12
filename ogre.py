from invader.invader import Invader


class Ogre(Invader):

    def __init__(self, invaderPropertiesFactory, canv, invader_path):
        Invader.__init__(self, canv, invader_path)
        self._invaderPropsFactory = invaderPropertiesFactory

    def setProperties(self):
        self.setMoveBehavior(self._invaderPropsFactory.createMoveBehavior())
        self.color = "red"

    def render(self):
        # Overrides super class render.  This is the template method.
        self._canv.delete(self._id)
        self._id = self._canv.create_rectangle(self._x - self._size, self._y - self._size,
                                          self._x + self._size, self._y + self._size,
                                          fill = self.color)

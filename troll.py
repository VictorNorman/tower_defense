from invader.invader import Invader


class Troll(Invader):

    def __init__(self, invaderPropertiesFactory, canv, invader_path):
        Invader.__init__(self, canv, invader_path)
        self._invaderPropsFactory = invaderPropertiesFactory

    def setProperties(self):
        self.setMoveBehavior(self._invaderPropsFactory.createMoveBehavior())
        self.color = "brown"

    def render(self):
        self._canv.delete(self._id)
        self._id = self._canv.create_oval(self._x - self._size, self._y - self._size,
                                          self._x + self._size, self._y + self._size,
                                          fill = self.color)

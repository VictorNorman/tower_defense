

class Invader:

    @staticmethod
    def createInvader(canv, invader_type, invader_path):
        if invader_type == "Ogre":
            from invader.ogre_factory import OgreInvaderFactory
            fact = OgreInvaderFactory()
        elif invader_type == "Troll":
            from invader.troll_factory import TrollInvaderFactory
            fact = TrollInvaderFactory()
        else:
            print("Don't have support for an invader of type -->" + invader_type + "<--")
            return
        return fact.makeSpecificInvader(canv, invader_path)

    def __init__(self, canvas, path):
        self._canv = canvas
        self._path = path

        self._size = 4   # radius of circle to draw (for now)

        # _dest_cell is the next cell's center that we are moving toward.
        # Start at the 0th cell, which may be off the screen.  Use it
        # to get your x, y value.  Then, find the 1st cell and use that to
        # set the x and y directions.
        self._dest_cell_idx = 0
        self._dest_cell = self._path.get_cell(0)
        self._x, self._y = self._dest_cell.get_center()

        self._compute_new_dir()

        # identifier for the circle we draw to represent the invader
        self._id = None
        self.moveBehavior = None
        self.color = None

    def startMovingOnPath(self):
        self.moveAndRender()

    def setMoveBehavior(self, moveBehavior):
        self.moveBehavior = moveBehavior

    def _compute_new_dir(self):
        '''Get (and remember) the next cell in that path, and then
        compute the xdir and ydir to get us from our current position
        to the center of that next cell.'''
        self._dest_cell_idx += 1
        if self._dest_cell_idx >= len(self._path):
            return
        self._dest_cell = self._path.get_cell(self._dest_cell_idx)
        d = self._dest_cell.get_center_x() - self._x
        if d > 0:
            self._xdir = 1
        elif d == 0:
            self._xdir = 0
        else:
            self._xdir = -1
        d = self._dest_cell.get_center_y() - self._y
        if d > 0:
            self._ydir = 1
        elif d == 0:
            self._ydir = 0
        else:
            self._ydir = -1

    def moveAndRender(self):
        self.move()
        self.render()  # template method: render defined in subclasses
        self._canv.after(30, self.moveAndRender)

    def move(self):
        # if we've arrived at the center, then compute the
        # direction to the next square on the path.
        if (self._x, self._y) == self._dest_cell.get_center():
            self._compute_new_dir()
        self.moveBehavior.move(self)

    def render(self):
        raise NotImplementedError("Must be implemented in subclass")


    def update_x(self, val):
        self._x += val
    def update_y(self, val):
        self._y += val
    def get_xdir(self): return self._xdir
    def get_ydir(self): return self._ydir

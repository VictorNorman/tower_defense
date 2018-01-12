from tkinter import *
from interface import implements
from subject import Subject


class Cell(implements(Subject)):

    TYPE2COL = { 'path': 'brown', 'tower': 'black', 'other': 'white' }

    def __init__(self, canvas, x, y, size, type='other'):
        self._canv = canvas
        self._x = x
        self._y = y
        self._size = size
        self._ulx = x * size          # upper-left x
        self._lrx = self._ulx + size  # lower-right x
        self._uly = y * size          # upper-left y
        self._lry = self._uly + size  # lower-right y
        self._tag = "cell" + str(x) + str(y)
        self._id = None
        self._type = None   # use subclassing?
        # True when the mouse is in this cell.
        self._mouseIn = False
        self._tower_placement_mode = False
        self._tower_being_placed = None
        self.set_type(type)
        self._id = self._canv.create_rectangle(self._ulx, self._uly, self._lrx, self._lry,
                                               fill=Cell.TYPE2COL[self._type], tag=self._tag)
        self._canv.tag_bind(self._id, "<Enter>", self.highlight)
        self._canv.tag_bind(self._id, "<Leave>", self.clear)
        self._canv.tag_bind(self._id, "<Button-1>", self.handleClick)

        # Needed for Subject implementation
        self._observers = []


    def clear(self, event=None):
        self._mouseIn = False
        if self._tower_placement_mode:
            self._canv.delete(self._rangeCircleId)
        self._canv.itemconfig(self._id, fill=Cell.TYPE2COL[self._type])

    def highlight(self, event=None):
        # Show green where the mouse is.
        self._canv.itemconfig(self._id, fill='green')
        self._mouseIn = True
        if self._tower_placement_mode:
            range_size = self._tower_being_placed.get_range()
            self._rangeCircleId = \
                self._canv.create_oval(self.get_center_x() - range_size, self.get_center_y() - range_size,
                                       self.get_center_x() + range_size, self.get_center_y() + range_size,
                                       outline="black")


    def registerObserver(self, observer):
        self._observers.append(observer)

    def removeObserver(self, observer):
        self._observers.remove(observer)

    def notifyObservers(self):
        for o in self._observers:
            o.update(self)

    def handleClick(self, event=None):
        self.notifyObservers()

    def __contains__(self, xy):
        '''Return True if the given x,y tuple is in the rectangle, False
        otherwise.'''
        x, y = xy
        return self._ulx < x < self._lrx and self._uly < y < self._lry

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

    def get_center(self):
        return self.get_center_x(), self.get_center_y()

    def get_center_x(self):
        return self._ulx + (self._size / 2)
    def get_center_y(self):
        return self._uly + (self._size / 2)

    def set_type(self, type):
        assert type in ('path', 'tower', 'other')
        self._type = type     # should use sub-class?
        if self._id is not None:
            self._canv.itemconfig(self._id, fill=Cell.TYPE2COL[self._type])

    def enable_tower_placement_mode(self, tower):
        self._tower_placement_mode = True
        self._tower_being_placed = tower
    def disable_tower_placement_mode(self):
        self._tower_placement_mode = False
        self._tower_being_place = None

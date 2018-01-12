from tkinter import *
from cell import Cell
from path import Path
from wave import Wave
from tower import  Tower

from interface import implements
from cell_observer import CellObserver


CANVAS_DIM = 600
SQUARE_SIZE = 30
NUM_CELLS_PER_DIM = int(CANVAS_DIM / SQUARE_SIZE)

TIME_BETWEEN_WAVES = 10    # seconds
INIT_GOLD_AMOUNT = 100


class App(implements(CellObserver)):

    def __init__(self, root):

        self._root = root
        self._gameRunning = False
        # TODO: probably move these into a Wave object?
        self._currWaveNumber = 0
        self._currWave = None
        self._path = None

        self._createGUIElements(root)

        self.grid = self._createGridOfCells()

        # Read path info from a file and highlight the path on the screen.
        self.readPathInfo()

        # TODO: should support multiple paths eventually.
        # TODO: _wave should be related to _currWave
        self._wave = Wave("wave1.txt", self._path, self._canv)


    def _createGUIElements(self, root):

        self._bottom_panel = Frame(root)
        self._bottom_panel.pack()
        self._btStartGame = Button(self._bottom_panel, text="Start Game",
                                   command=self.startGame)
        self._btStartGame.pack(side=LEFT)
        Label(self._bottom_panel, text="Gold: ").pack(side=LEFT)
        self._goldAmtVar = IntVar()
        self._goldAmtVar.set(INIT_GOLD_AMOUNT)
        self._goldLbl = Label(self._bottom_panel, textvariable=self._goldAmtVar)
        self._goldLbl.pack(side=LEFT)
        self._btNextWave = Button(self._bottom_panel, text="Start Wave",
                                  command=self.startNextWave, state=DISABLED)
        self._btNextWave.pack(side=LEFT)
        Label(self._bottom_panel, text="Time till next wave starts: ").pack(side=LEFT)
        self._timeLeftTilWave = IntVar()
        self._timeLeftTilWave.set(TIME_BETWEEN_WAVES)
        self._timeLeftLbl = Label(self._bottom_panel, textvariable=self._timeLeftTilWave)
        self._timeLeftLbl.pack(side=LEFT)
        self._btPlaceTower = Button(self._bottom_panel, text="Place tower",
                                    command=self.placeTowerMode, state=DISABLED)
        self._btPlaceTower.pack(side=LEFT)
        self._canv = Canvas(root, width=CANVAS_DIM, height=CANVAS_DIM)
        self._canv.pack()

    def startGame(self):
        self._gameRunning = True
        self._btNextWave.config(state=NORMAL)
        self._btStartGame.config(state=DISABLED)
        self._btPlaceTower.config(state=NORMAL)
        # Start the timer, which forces the next wave to start in a few seconds.
        self._canv.after(1000, self.decrementTimer)

    def startNextWave(self):
        '''Start the next wave now, instead of waiting for the timer to go down to 0.'''
        if not self._gameRunning:
            return
        self._timeLeftTilWave.set(TIME_BETWEEN_WAVES)
        self._wave.start()
        self._canv.after(1000, self.decrementTimer)

    def decrementTimer(self):
        timeLeft = self._timeLeftTilWave.get() - 1
        self._timeLeftTilWave.set(timeLeft)
        if timeLeft == 0:
            self.startNextWave()
        else:
            self._canv.after(1000, self.decrementTimer)

    def readPathInfo(self):
        '''Read path information from a file and create a path object for it.'''
        self._path = Path(NUM_CELLS_PER_DIM)
        with open('path.txt') as pf:
            for elem in pf:
                elem = elem.strip()
                x, y = map(int, elem.split(','))   # map(int) to make ints.
                self._path.add_cell(self.grid[y][x])
                self.grid[y][x].set_type('path')

    def update(self, cell):
        # print("cell at {}, {} clicked".format(cell.get_x(), cell.get_y()))
        cell.set_type("tower")
        self.disableAllCellsTowerPlacementMode()
        self._btPlaceTower.config(state=NORMAL)
        self._placingATower = False
        # self.towers.append(Tower(cell.get_x(), cell.get_y()...))

    def _createGridOfCells(self):
        grid = []
        for row in range(NUM_CELLS_PER_DIM):
            rowlist = []
            for col in range(NUM_CELLS_PER_DIM):
                cell = Cell(self._canv, col, row, SQUARE_SIZE)
                rowlist.append(cell)
                # register to receive notifications when a cell is clicked
                cell.registerObserver(self)
            grid.append(rowlist)
        return grid

    def placeTowerMode(self):
        self._placingATower = True
        self._btPlaceTower.config(state=DISABLED)
        self.enableAllCellsTowerPlacementMode()

    def enableAllCellsTowerPlacementMode(self):
        t = Tower(0, 0)
        for r in self.grid:
            for cell in r:
                cell.enable_tower_placement_mode(t)

    def disableAllCellsTowerPlacementMode(self):
        for r in self.grid:
            for cell in r:
                cell.disable_tower_placement_mode()

root = Tk()
root.title("Calvin Tower Defense")
App(root)
root.resizable(width=False, height=False)
root.wm_attributes('-topmost', 1)
print(root.geometry())
root.mainloop()

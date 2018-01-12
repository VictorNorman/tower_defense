from invader.invader import Invader

class Wave:
    '''A group of invaders'''
    def __init__(self, fileToReadFrom, paths, canv):
        # TODO: current paths is just a single path object.  Eventually, use
        # the path number from the wave file to index into a list of paths.
        self._canv = canv
        self._invaders = []
        self._timeBetweenInvaders = []
        with open(fileToReadFrom, "r") as w:
            for line in w:
                line = line.strip()
                if line == "":
                    continue   # skip empty line
                if line.startswith("#"):
                    continue   # skip empty line
                fields = line.split(',')
                # fields[0] is the path, fields[1] is the invader name, fields[2] is the time between
                # starting invaders on the path.
                self._invaders.append(Invader.createInvader(canv, fields[1].strip(), paths))
                self._timeBetweenInvaders.append(int(fields[2]))

        self._nextInvader = 0  # keep track of which invader to send on the path next.
        self._path = paths   # TODO: just supports 1 path at this time.



    def start(self):
        self._nextInvader = 0
        self._startNextInvader()


    def _startNextInvader(self):
        self._invaders[self._nextInvader].startMovingOnPath()
        self._nextInvader += 1
        if self._nextInvader < len(self._timeBetweenInvaders):
            self._canv.after(self._timeBetweenInvaders[self._nextInvader], self._startNextInvader)





class InvaderFactory:
    def createInvader(self, canv, invader_path):
        raise NotImplementedError()

    def makeSpecificInvader(self, canv, invader_path):
        inv = self.createInvader(canv, invader_path)   # ??
        inv.setProperties()
        return inv

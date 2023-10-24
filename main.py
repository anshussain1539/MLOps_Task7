#testing2

class Bulb:
    status = 0

    def isVisible(self):
        if self.status == 0:
            return False
        else:
            return True
        
    def isOn(self):
        if self.status == 0:
            self.status = 1
        else:
            pass

    def isOff(self):
        if self.status == 1:
            self.status = 0
        else:
            pass

    def getStatus(self):
        if self.status == 0:
            return "Bulb is not glowing"
        else:
            return "Bulb is glowing"





class Position:
    xyCoordinates = tuple()
    #yCoordinates = 0

    def __init__(self, xyCoordinates):
        if len(xyCoordinates) != 2:
            raise Exception("Invalid coordinates")
         #   xCoordinates = 0
         #  yCoordinates = 0
        self.xyCoordinates = xyCoordinates
        #self.yCoordinates = yCoordinates



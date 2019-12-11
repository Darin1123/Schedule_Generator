class Point(object):
    def __init__(self, x, y):
        self.__x = x;
        self.__y = y

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def setX(self, newX):
        self.__x = newX

    def setY(self, newY):
        self.__y = newY

    def __hash__(self):
        return 10*self.__x+self.__y

    def __eq__(self, that):
        return self.__hash__()==that.__hash__()

    def __ne__(self, that):
        return not self.__eq__(that)

    def __repr__(self):
        return "("+str(self.x())+", "+str(self.y())+")"
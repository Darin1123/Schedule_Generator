import util

class Point(object):
	def __init__(self, x, y):
		self.__x = x;
		self.__y = y

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

	def setX(self, newX):
		self.__x = newX

	def setY(self, newY):
		self.__y = newY

	def compareTo(self, that):
		thisX = self.getX()
		thatX = that.getX()
		compareX = util.compareInt(thisX, thatX)
		if compareX!=0:
			return compareX
		else:
			thisY = self.getY()
			thatY = that.getY()
			return util.compareInt(thisY, thatY)

	def __hash__(self):
		return 10*self.getX()+self.getY()

	def __eq__(self, that):
		return self.__hash__()==that.__hash__()

	def __ne__(self, that):
		return not self.__eq__(that)

	def __repr__(self):
		return "("+str(self.getX())+", "+str(self.getY())+")"


if __name__ == '__main__':
	p1 = Point(1, 2)
	p2 = Point(1, 2)

	s1 = set()
	s1.add(p1)
	s2 = set()
	s2.add(p2)

	print(p1==p2)





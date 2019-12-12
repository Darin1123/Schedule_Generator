class Schedule:
    def __init__(self):
        self.__table = []
        self.init()
    
    def init(self):
        for i in range(5):
            self.__table.append([])
            for j in range(11):
                self.__table[i].append(None)
                
    def getTable(self):
        return self.__table.copy()
    
    def insertCourseInstance(self, instance):
        for lec in instance.lec:
            self.__table[lec.x()][lec.y()]=(instance.name, 'lec '+str(instance.ids['lecid']))
        for tut in instance.tut:
            self.__table[tut.x()][tut.y()]=(instance.name, 'tut '+str(instance.ids['tutid']))
        for lab in instance.lab:
            self.__table[lab.x()][lab.y()]=(instance.name, 'lab '+str(instance.ids['labid']))
            
    def insertCourseInstances(self, instances):
        for i in instances:
            self.insertCourseInstance(i)
class CourseInstance:
    def __init__(self, name, lec, tut, lab, lecid, tutid, labid):
        self.name = name
        self.ids = {}
        self.ids['lecid'] = lecid
        self.ids['tutid'] = tutid
        self.ids['labid'] = labid
        self.lec = self.__prepare(lec)
        self.tut = self.__prepare(tut)
        self.lab = self.__prepare(lab)
        
    def __prepare(self, part):
        if part==None:
            return set()
        return part
        
    def merge(self):
        return self.lec|self.tut|self.lab
        
    def __repr__(self):
        return self.name+'\nLec: '+str(self.lec)+'\nTut: '+str(self.tut)+'\nLab: '+str(self.lab)+'\n'
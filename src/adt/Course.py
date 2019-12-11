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
        

##
# @brief given a list of course instances, return if there exist conflict(s)
# @param cis list of CourseInstance's
# @return Boolean
def hasConflict(cis):
    for i in range(len(cis)):
        for j in range(i+1, len(cis)):
            temp = cis[i].merge()&cis[j].merge()
            if len(temp)!=0:
                return True
    return False

class Course:
    def __init__(self, name):
        self.__name = name
        self.__lecs = [None]
        self.__tuts = [None]
        self.__labs = [None]
        
    
    def getName(self):
        return self.__name
    
    def getLecs(self):
        return self.__lecs.copy()
    
    def getTuts(self):
        return self.__tuts.copy()
    
    def getLabs(self):
        return self.__labs.copy()
    
    def __addSec(self, part, section):
        if part[0]==None:
            part[0]=section
        else:
            part.append(section)
            
    def addLec(self, section):
        self.__addSec(self.__lecs, section)
    
    def addTut(self, section):
        self.__addSec(self.__tuts, section)
            
    def addLab(self, section):
        self.__addSec(self.__labs, section)
    
    ##
    # @brief A function that returns all possibilities that a Course can generate
    # @param None
    # @return a list of CourseInstances
    def generateCourseInstances(self):
        generated = []
        lecs = self.getLecs()
        tuts = self.getTuts()
        labs = self.getLabs()
        for c_ in range(len(lecs)):
            for t_ in range(len(tuts)):
                for l_ in range(len(labs)):
                    generated.append(CourseInstance(self.getName(), lecs[c_], tuts[t_], labs[l_], c_+1, t_+1, l_+1))
        return generated
        
    def __repr__(self):
        return self.getName()+'\nLecs: '+str(self.getLecs())+'\nTuts: '+str(self.getTuts())+'\nLabs: '+str(self.getLabs())+'\n'
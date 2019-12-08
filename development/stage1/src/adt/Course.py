from .CourseInstance import *

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
from adt.Point import *
from adt.Course import *
from adt.CourseInstance import *
from adt.Schedule import *
from util import *

##
# @param list of Course's
# @return list of Schedule's 
def generateSchedules(courses):
    #generate cis array
    cisArray=[]
    for c in courses:
        cisArray.append(c.generateCourseInstances())
        
    #init seed
    seed = []
    for ci in cisArray[0]:
        seed.append([ci])
        
    #map all courses
    for i in range(1, len(cisArray)):
        seed = map(seed, cisArray[i])
    
    #generate all possible schedules
    schedules = []
    for i in seed:
        if not hasConflict(i):
            tempSch = Schedule()
            tempSch.insertCourseInstances(i)
            schedules.append(tempSch)
    return schedules

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
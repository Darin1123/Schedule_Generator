from adt.Schedule import Schedule
from adt.Course import hasConflict
from util import map

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
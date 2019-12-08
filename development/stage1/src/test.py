from adt.Point import *
from adt.Course import *
from adt.CourseInstance import *
from adt.Schedule import *
from util import *

def sampleCourse():
    c = Course('4ac3')
    lec1 = set()
    lec1.add(Point(0, 3))
    lec1.add(Point(2, 3))
    lec1.add(Point(4, 5))
    c.addLec(lec1)
    tut = set()
    tut.add(Point(3, 1))
    c.addTut(tut)
    return c

def sampleCourse1():
    c = Course('4ml3')
    lec = set()
    lec.add(Point(3, 6))
    lec.add(Point(3, 7))
    lec.add(Point(1, 8))
    c.addLec(lec)
    tut = set()
    tut.add(Point(1, 2))
    c.addTut(tut)
    return c

def sampleCourse2():
    c = Course('4c03')
    lec = set()
    lec.add(Point(0, 9))
    lec.add(Point(2, 9))
    lec.add(Point(3, 9))
    c.addLec(lec)
    lab = set()
    lab.add(Point(2, 6))
    lab.add(Point(2, 7))
    lab.add(Point(2, 8))
    c.addLab(lab)
    return c

def sampleCourse3():
    c = Course('4X03')
    lec = set()
    lec.add(Point(1, 4))
    lec.add(Point(2, 4))
    lec.add(Point(4, 4))
    c.addLec(lec)
    tut = set()
    tut.add(Point(0, 5))
    c.addTut(tut)
    return c

def hasConflict(cis):
    for i in range(len(cis)):
        for j in range(i+1, len(cis)):
            temp = cis[i].merge()&cis[j].merge()
            if len(temp)!=0:
                return True
    return False

##
# @param a 2d array
# @param b 1d array
# @return 2d array
def map(a, b):
    res = []
    for i in a:
        for j in b:
            i_ = i + [j]
            res.append(i_)
    return res

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

c1 = sampleCourse()
c2 = sampleCourse1()
c3 = sampleCourse2()
c4 = sampleCourse3()
schedules = generateSchedules([c1, c2, c3, c4])
if (len(schedules)==0):
    print("There exists cinflict.")
else:
    print(str(len(schedules))+" schedule(s) generated.")
for i in range(len(schedules)):
    writeSchedule(schedules[i], 'schedule '+str(i))
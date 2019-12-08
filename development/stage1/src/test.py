from adt.Point import *
from adt.Course import *
from adt.CourseInstance import *
from adt.Schedule import *
from util import *
from mainFunc import *
from file import *

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
    c = Course('4x03')
    lec = set()
    lec.add(Point(1, 4))
    lec.add(Point(2, 4))
    lec.add(Point(4, 4))
    c.addLec(lec)
    tut = set()
    tut.add(Point(0, 5))
    c.addTut(tut)
    return c

# import csv

# def writeSchedule(schedule, fileName):
#     headers = ['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursay', 'Friday']
#     table = schedule.getTable()
#     rows = []
#     for i in range(10):
#         row = [convertTime(i)]
#         for j in range(5):
#             row.append(table[j][i])
#         rows.append(row)
        
#     with open(fileName+".csv", 'w') as f:
#         f_csv = csv.writer(f)
#         f_csv.writerow(headers)
#         f_csv.writerows(rows)

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
    writeSchedule(schedules[i], 'schedule_'+str(i))
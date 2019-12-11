from adt.Point import Point
from adt.Course import Course
from mainFunc import generateSchedules
from file import writeSchedule
from util import day2num
import sys

def getNumCourses():
    numCourse = input('> Enter number of courses: ')
    try:
        num = int(numCourse)
        if num<=0:
            printInstruction('[!] Invalid number.')
            return getNumCourses() 
        return num 
    except:
        printInstruction('[!] Please enter a number.')
        return getNumCourses()

def getNumSecs(courseName, sectype):
    numLec = input('> %s: Enter number of %s sections: '%(courseName, sectype))
    try:
        num = int(numLec)
        if num<0:
            printInstruction('[!] Invalid number.')
            return getNumSecs(courseName, sectype) 
        return num 
    except:
        printInstruction('[!] Please enter a number.')
        return getNumSecs(courseName, sectype)

def createSection(courseName, index, category):
    sec = set()
    print()
    print('[!] Example for days: TuWe')
    print('[!] Example for "9:30-10:20": 9-10 ')
    print('[!] A complete example: "MoWeTh 17-18, Tu 12-13"')
    print()
    data = input('%s %s_%d > Enter day(s) and time(s): '%(courseName, category, index))
    lines = data.split(',')
    for line in lines:
        line = line.strip()
        data = line.split(' ')
        days = data[0]
        time = data[1]
        try:
            lenDays = len(days)
            if lenDays%2!=0:
                print('[!] There exist errors in the days')
            else:
                xs = []
                for i in range(0, lenDays, 2):
                    day = days[i: i+2]
                    print(day)
                    xs.append(day2num(day))
            times = time.split('-')
            start = int(times[0])
            to = int(times[1])
            print('from: %d'%(start))
            print('to: %d'%(to))
            last = to-start
            ys = []
            for i in range(last):
                ys.append(start-8+i)
            for x in xs:
                for y in ys:
                    sec.add(Point(x, y))
        except:
            print('[!] There exist errors in the input')
            print()
            return createSection(courseName, index, category)
    return sec

def main():
    print('')
    print("=====================================")
    print("=  Welcome to Course Manager 0.0.4  =")
    print("=====================================")
    print()
    print('[!] Follow the instructions to create your timetable')
    print()
    
    num = getNumCourses()
    courses = []
    for i in range(num):
        courseName = input('> Enter course_%d\'s name: '%(i+1))
        tempCourse = Course(courseName)
        numLecs = getNumSecs(courseName, 'lecture')
        for c in range(numLecs):
            tempLecSec = createSection(courseName, c+1, 'lecture')
            tempCourse.addLec(tempLecSec)
        numTuts = getNumSecs(courseName, 'tutorial')
        for t in range(numTuts):
            tempTutSec = createSection(courseName, t+1, 'tutorial')
            tempCourse.addTut(tempTutSec)
        numLabs = getNumSecs(courseName, 'lab')
        for l in range(numLabs):
            tempLabSec = createSection(courseName, l+1, 'lab')
            tempCourse.addLab(tempLabSec)
        courses.append(tempCourse)
    schedules = generateSchedules(courses)
    if (len(schedules)==0):
        print("There exists cinflict.")
    else:
        for i in range(len(schedules)):
            writeSchedule(schedules[i], './schedule_'+str(i))
    print(str(len(schedules))+" schedule(s) generated.")



if __name__ == '__main__':
    main()

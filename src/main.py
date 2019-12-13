from adt.Point import Point
from adt.Course import Course
from mainFunc import generateSchedules
from file import writeSchedule
from util import day2num
import sys
import os

def getNumCourses():
    numCourse = input('> Enter number of courses: ')
    try:
        num = int(numCourse)
        if num<=0:
            print('[!] Invalid number.')
            print()
            return getNumCourses() 
        return num 
    except:
        print('[!] Please enter a number.')
        print()
        return getNumCourses()

def getNumSecs(courseName, sectype):
    numLec = input('> %s: Enter number of %s sections: '%(courseName, sectype))
    try:
        num = int(numLec)
        if num<0:
            print('[!] Invalid number.')
            print()
            return getNumSecs(courseName, sectype) 
        return num 
    except:
        print('[!] Please enter a number.')
        print()
        return getNumSecs(courseName, sectype)

def createSection(courseName, index, category, f):
    sec = set()
    print()
    print('[!] Example for days: TuWe')
    print('[!] Example for "9:30-10:20": 9-10 ')
    print('[!] A complete example: "MoWeTh 17-18, Tu 12-13"')
    print()
    f.write('%s_%d: '%(category, index))
    data = input('%s %s_%d > Enter day(s) and time(s): '%(courseName, category, index))
    print(data)
    f.write(data+'\n')
    lines = data.split(',')
    for line in lines:
        line = line.strip()
        data = line.split(' ')
        try:
            days = data[0]
            time = data[1]
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
            if to<start:
                print('[!] End time must be after start time.')
                print()
                return createSection(courseName, index, category, f)
            if start<8:
                print('[!] Start time must be after or equal to 8.')
                print()
                return createSection(courseName, index, category, f)
            if start>19:
                print('[!] Start time must be before or equal to 19.')
                print()
                return createSection(courseName, index, category, f)
            if start==18:
                print('[!] Class never starts on 18.')
                print()
                return createSection(courseName, index, category, f)
            if to<9:
                print('[!] End time must be before or equal to 9.')
                print()
                return createSection(courseName, index, category, f)
            if start==19 and to!=22:
                print('[!] End time must be equal to 22.')
                print()
                return createSection(courseName, index, category, f)
            if start<=17 and to>18:
                print('[!] End time must be before or equal to 18.')
                print()
                return createSection(courseName, index, category, f)
            print('from: %d'%(start))
            print('to: %d'%(to))
            print()
            ys = []
            if start<17:
                last = to-start
                for i in range(last):
                    ys.append(start-8+i)
            else:
                ys.append(10)
            for x in xs:
                for y in ys:
                    sec.add(Point(x, y))
        except:
            print('[!] There exist errors in the input')
            print()
            return createSection(courseName, index, category, f)
    return sec

def main():
    print('')
    print("=====================================")
    print("=  Welcome to Course Manager 0.0.4  =")
    print("=====================================")
    print()
    print('[!] Follow the instructions to create your timetable')
    print()
    
    termName = input('> Enter term name: ')
    print(termName)
    print()
    pwd = sys.argv[0]
    paths = pwd.split('/')
    rebuildPath = ''
    for i in range(len(paths)-1):
        rebuildPath+=paths[i]+'/'
    f = open(rebuildPath+termName+'.txt', 'w')
    f.write(termName+'\n')
    num = getNumCourses()
    print(num)
    print()
    f.write('number of courses: '+str(num)+'\n')
    courses = []
    for i in range(num):
        courseName = input('> Enter course_%d\'s name: '%(i+1))
        print(courseName)
        print()
        f.write('course_%d\'s name: %s\n'%(i+1, courseName))
        tempCourse = Course(courseName)
        numLecs = getNumSecs(courseName, 'lecture')
        print(numLecs)
        print()
        f.write('# lectures: %d\n'%(numLecs))
        for c in range(numLecs):
            tempLecSec = createSection(courseName, c+1, 'lecture', f)
            tempCourse.addLec(tempLecSec)
        numTuts = getNumSecs(courseName, 'tutorial')
        print(numLecs)
        print()
        f.write('# tuts: %d\n'%(numTuts))
        for t in range(numTuts):
            tempTutSec = createSection(courseName, t+1, 'tutorial', f)
            tempCourse.addTut(tempTutSec)
        numLabs = getNumSecs(courseName, 'lab')
        print(numLabs)
        print()
        f.write('# labs: %d\n'%(numLabs))
        for l in range(numLabs):
            tempLabSec = createSection(courseName, l+1, 'lab', f)
            tempCourse.addLab(tempLabSec)
        courses.append(tempCourse)
        f.write("END\n")
    schedules = generateSchedules(courses)
    if (len(schedules)==0):
        print("There exists conflict.")
    else:
    	check = input("[!] Warning: existing schedules may be overwritten, enter 'yes' to continue, other to stop.\n> ")
    	print()
    	if check=='yes':
            try:
                os.mkdir(rebuildPath+'schedules')
            except:
                print('[!] overwrite files in folder \'schedules\'')
                print()
            for i in range(len(schedules)):
                writeSchedule(schedules[i], './schedules/schedule_'+str(i+1))
            print(str(len(schedules))+" schedule(s) generated.")
            print()
    f.close()



if __name__ == '__main__':
    main()
    #print(sys.argv[0])

import csv

def writeSchedule(schedule, fileName):
    headers = ['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursay', 'Friday']
    table = schedule.getTable()
    rows = []
    for i in range(10):
        row = [convertTime(i)]
        for j in range(5):
            row.append(table[j][i])
        rows.append(row)
        
    with open(fileName+".csv", 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

def convertDay(day):
    switcher = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday"
    }
    return switchertcher[day]

def convertTime(time):
    switcher ={
        0: "8:30=9:20",
        1: "9:30-10:20",
        2: "10:30-11:20",
        3: "11:30-12:20",
        4: "12:30-13:20",
        5: "13:30-14:20",
        6: "14:30-15:20",
        7: "15;30-16:20",
        8: "14:30-17:20",
        9: "17:30-18:20"
    }
    return switcher[time]
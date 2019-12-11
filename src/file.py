import csv
from util import convertDay, convertTime

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
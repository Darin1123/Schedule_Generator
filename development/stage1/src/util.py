##
# @brief convert a digit to a weekday
# @param day int
# @return string
def convertDay(day):
    switcher = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday"
    }
    return switchertcher[day]

##
# @brief convert a digit to a period
# @param time int
# @return string
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

##
# Example:
#
#   a=[[1, 2],   b=[5,
#      [3, 4]]      6]
#   
#   map(a, b)=[[1, 2, 5],
#              [1, 2, 6],
#              [3, 4, 5],
#              [3, 4, 6]]
#
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
"""
def solution(a, b):

    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    if a==1:
        return day[(b-1)%7]
    elif a==2:
        return day[(b+31-1)%7]
    elif a==3:
        return day[(b+60-1)%7]
    elif a==4:
        return day[(b+91-1)%7]
    elif a==5:
        return day[(b+121-1)%7]
    elif a==6:
        return day[(b+151-1)%7]
    elif a==7:
        return day[(b+181-1)%7]
    elif a==8:
        return day[(b+212-1)%7]
    elif a==9:
        return day[(b+243-1)%7]
    elif a==10:
        return day[(b+273-1)%7]
    elif a==11:
        return day[(b+304-1)%7]
    elif a==12:
        return day[(b+334-1)%7]

"""
import datetime
def solution(a, b):
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    week_day = datetime.datetime(2016, a, b).weekday()

    return day[week_day]

import datetime
def solution(a, b):
    answer = ''
    days = {0: 'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    day = datetime.date(2016,a,b)
    return days[day.weekday()]
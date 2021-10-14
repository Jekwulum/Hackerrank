import calendar as cal
"""
since weekdays start with Monday as 0 in the calendar module, 
we declare a list with weekdays beginning from Monday as it's 0th index
"""
wk_day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def year_constraint(year):
    if year in range(2000, 3001):
        return True

mm, dd, yyyy = map(int, input().strip().split(" "))

if year_constraint(yyyy):
    wk_day = cal.weekday(yyyy, mm, dd)
    day_name = wk_day_list[wk_day]
    print(day_name.upper())


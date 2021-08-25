def is_leap(year):
    leap = False
    
    if year in range(1900, 100001):
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 == 0:
                    leap = True
            else:
                leap = False
    return leap


if __name__ == '__main__':
    
    year = int(input())
    print(is_leap(year))

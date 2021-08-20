

def integers(a,b,c,d):
    if a not in range(1, 1001):
        return
    if b not in range(1, 1001):
        return
    if c not in range(1, 1001):
        return
    if d not in range(1, 1001):
        return
    print(a**b + c**d)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    integers(a,b,c,d)

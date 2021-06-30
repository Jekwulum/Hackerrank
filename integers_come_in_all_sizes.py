
def integers(a,b,c,d):
    while a and b and c and d in range(1,1000):
        print(a**b + c**d)
        break


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    integers(a,b,c,d)

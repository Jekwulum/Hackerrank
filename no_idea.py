
def check_length(my_arr, A, B): # constraints
    if n in range(1, 10**5 + 1) and m in range(1, 10**5 + 1):
        if len(my_arr) <= n and len(A) <= m and len(B) <= m:
            return True
    else:
        return False   

def happy(my_arr, A, happiness):    # increase happiness by the number of times elements of A occur in my_arr
    myList = [x for x in my_arr if x in A]
    happiness += len(myList)
    return happiness

def not_happy(my_arr, B, happiness):    # decrease happiness by the number of times elements of B occur in my_arr
    myList = [x for x in my_arr if x in B]
    happiness -= len(myList)
    return happiness


happiness = 0 

n, m = map(int, input().split(" "))
my_arr = list(map(float, input().split(" ")))
A = set(map(float, input().split(" ")))
B = set(map(float, input().split(" ")))


if check_length(my_arr, A, B):  # if constraints are passed
    happiness = happy(my_arr, A, happiness)
    happiness = not_happy(my_arr, B, happiness)
print(happiness)

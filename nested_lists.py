n = int(input())

def get_2nd_lowest(args):
    val= sorted(set(args))[1]
    return val

def nested_list(n):
    if n not in range(2, 6):
        return
    
    my_list = []
    for _ in range(n):
        name = input()
        score =  float(input())
        new_list = [name, score]
        my_list.append(new_list)
    
    my_list = sorted(my_list)
    vals = []
    for i, j in my_list:
        vals.append(j)
    val = get_2nd_lowest(vals)
    for i, j in my_list:
        if j == val:
            print(i)
            
nested_list(n)



n = int(input())

def check_n(n):
    if n in range(2,11):
        # print("n in range")
        return True
    else:
        # print("n not in range")
        return
    return False
    
def check_scores(args): 
    if len(args) != 3:
        # print("length issue")
        return False
    
    for i in args:
        if i < 0:
            # print("i not in range")
            return False
        elif i > 100:
            return False
    return True

def avg(name, student_marks):
    scores = student_marks[name]
    avg_score = sum(scores)/3
    # print("avg working")
    return round(avg_score, 2)
    
def main(n):
    if check_n(n):
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            if check_scores(scores):
                student_marks[name] = scores
            else:
                return
            
        query_name = input()
        print("{:.2f}".format(avg(name=query_name, student_marks=student_marks)))

main(n)

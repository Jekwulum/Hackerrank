"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
"""





num = int(input('enter number of scores: '))
x = input('enter scores: ')

def check_repeat(val, args): # to check if max value is double and then remove if it is still remaining in list
    if val in args:             
        args.remove(val)
        check_repeat(val, args) # it is also a recursive function
    else:
        return

def check(x, num):
    arr = [int(i) for i in x.split()]
    # print(arr)
    if num < 2 or num > 10:
        return('num not in range 2 -> 10')
    if len(arr) > num:
        return('scores more than number of scores put in')
        
    elif len(arr) < num:
        return('scores less than number of scores put in')
        
    for i in arr:
        if i < -100 or i > 100:
            return('scores not in range of -100 -> 100')
            
    mx = max(arr)
    check_repeat(mx, arr)
    
    mx2 = max(arr)
    return '2nd runner up is: {}'.format(mx2)

print(check(x, num))

def mutate_string(string, position, character):
    post_2nd = position + 1                   
    
    new_line = string[:position] + character + string[post_2nd:]    
    return new_line

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

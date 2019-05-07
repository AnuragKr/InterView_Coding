def get_first_set_bit(input_num):
    pos = 1
    set_bit = 1
    while(not(set_bit & input_num)):
        set_bit = set_bit<<1
        pos = pos+1
    return pos
        
if __name__ == "__main__":
    no_of_test_case = int(input())
    list_of_input = []
    for _ in range(no_of_test_case):
        x,y = (map(int,input().split()))
        if(x == y):
            print(0)
        else:
            print(get_first_set_bit(x ^ y))
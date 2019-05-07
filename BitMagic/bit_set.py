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
        list_of_input.append(int(input()))
    for num in list_of_input:
        if(num == 0):
            print(0)
        elif(num == 1):
            print(1)
        else:
            print(get_first_set_bit(num))
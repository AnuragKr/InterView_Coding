
def countSetBits(num):  
     binary = bin(num) 
     set_bits = 0
     set_bits = [ones for ones in binary[2:] if ones=='1'] 
     return len(set_bits)
       
if __name__ == "__main__":
    test_cases = int(input())
    ans_list = []
    for _ in range(test_cases):
        a ,b = (map(int,input().split()))
        ans_list.append(a^b)
    
    for num in ans_list:
        print(countSetBits(num))

        
INT_BITS = 12

def leftRotate(n, d):  
    return (n << d)|(n >> (INT_BITS - d)) 
  
def rightRotate(n, d):  
    return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF

if __name__ == "__main__":
    test_cases = int(input())
    ans_list = []
    for _ in range(test_cases):
        a ,b = (map(int,input().split()))
        ans_list.append(leftRotate(a,b))
        ans_list.append(rightRotate(a,b))
        
    for num in ans_list:
        print(num)
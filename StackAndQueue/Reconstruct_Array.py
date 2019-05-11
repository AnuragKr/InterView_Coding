def reconstruct(array):
    answer = []
    n = len(array) - 1
    stack = []

    for i in range(n):
        if array[i+1] == '-':
            print(i)
            stack.append(i)
        else:
            answer.append(i)
            while stack:
                answer.append(stack.pop())
    
    stack.append(n)

    while stack:
        answer.append(stack.pop())
    return answer

if __name__ == "__main__":
    print(reconstruct([None,"+","-","-","-"]))
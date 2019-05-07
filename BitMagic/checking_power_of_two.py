if __name__ == "__main__":
    no_of_test_case = int(input())
    list_of_input = []
    for _ in range(no_of_test_case):
        list_of_input.append(int(input()))
    for num in list_of_input:
        if(num & (num-1)):
            print("NO")
        else:
            print("YES")
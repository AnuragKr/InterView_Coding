def window(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(n):
        max_seen = max(max_seen, array[i])
        print(max_seen)
        if array[i] < max_seen:
            right = i

    for i in range(n-1, -1, -1):
        min_seen = min(min_seen, array[i])
        print(min_seen)
        if array[i] > min_seen:
            left = i

    return left, right


if __name__ == "__main__":
    input_list = [3, 7, 5, 6, 9]
    print(window(input_list))

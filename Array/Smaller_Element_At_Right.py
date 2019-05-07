import bisect


def smaller_counts_naive(lst):
    result = []
    for i, num in enumerate(lst):
        count = sum(val < num for val in lst[i+1:])
        result.append(count)
    return result


def smaller_counts(lst):
    result = []
    seen = []

    for num in reversed(lst):
        i = bisect.bisect_left(seen, num)
        print(seen, num, i)
        result.append(i)
        bisect.insort(seen, num)
        print(seen)

    return list(reversed(result))


if __name__ == "__main__":
    input_list = [3, 4, 9, 6, 1]
    print(smaller_counts(input_list))

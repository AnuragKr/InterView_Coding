def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0

    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far


def min_subarray_sum(arr):
    min_ending_here = min_so_far = 0

    for x in arr:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_ending_here, min_so_far)
    return min_so_far


def maximum_circular_subarray(arr):
    max_subarray_sum_wraparound = sum(arr) - min_subarray_sum(arr)
    return max(max_subarray_sum(arr), max_subarray_sum_wraparound)


if __name__ == "__main__":
    input_list = [8, -1, 3, 4]
    print(max_subarray_sum(input_list))
    print(sum(input_list),min_subarray_sum(input_list))
    print(maximum_circular_subarray(input_list))

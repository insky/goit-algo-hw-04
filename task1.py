from timeit import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return _merge(merge_sort(left_half), merge_sort(right_half))

def _merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def timsort(arr):
    return sorted(arr)


def main():
    data_sizes = [10, 100, 1000, 10000, 100000]
    sorting_algorithms = {
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Timsort': timsort
    }

    for size in data_sizes:
        data = [random.randint(0, 10000) for _ in range(size)]
        print(f"\nArray Size: {size}")
        for name, sort_func in sorting_algorithms.items():
            time_taken = timeit(lambda: sort_func(data.copy()), number=1)
            print(f"{name}: {time_taken:.6f} seconds")


if __name__ == "__main__":
    main()

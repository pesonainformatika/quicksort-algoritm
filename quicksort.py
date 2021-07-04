def partisi(arr: list, low: int, high: int) -> int:
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr: list, low: int, high: int):
    if len(arr) == 1:
        return arr
    if low < high:
        p1 = partisi(arr, low, high)
        # mengurutkan dengan quicksort
        quicksort(arr, low, p1 - 1)
        quicksort(arr, p1 + 1, high)


if __name__ == '__main__':
    array_list = [10, 7, 8, 9, 1, 5]
    n = len(array_list)
    quicksort(array_list, 0, n - 1)
    print(f'array yang sedang diurutkan')
    for i in range(n):
        print(f'{array_list[i]}')

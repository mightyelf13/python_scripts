def bi(arr, target, first_occurrence):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            if first_occurrence:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def occurrences(sorted, look_for):
    occurrences = []
    for n in look_for:
        first_occurrence = bi(sorted, n, True)
        last_occurrence = bi(sorted, n, False)
        if first_occurrence != -1 and last_occurrence != -1:
            count = last_occurrence - first_occurrence + 1
            occurrences.append(count)
        else:
            occurrences.append(0)

    return occurrences


if __name__ == "__main__":
    N = int(input())
    sequence = list(map(int, input().split()))

    search = list(map(int, input().split()))

    result = occurrences(sequence, search)

    for count in result:
        print(count)

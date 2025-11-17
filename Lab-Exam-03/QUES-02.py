def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        # print(f"left: {left}, right: {right}, mid: {mid}, arr[mid]: {arr[mid]}")  # Debug

        if arr[mid] == target:
            return mid  # Found, return index
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    return -1  # Not found

# Testing the binary_search function
arr = [10, 20, 30, 40, 50, 60]
target = 30

result = binary_search(arr, target)
if result != -1:
    print(f"Number {target} found at index {result}")
else:
    print(f"Number {target} not found in the array")
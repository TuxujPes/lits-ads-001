def merge_sort(array):
    return merge_sort_internal(array, 0, len(array)-1)

def merge_sort_internal(array, left, right):
    if right > left:
        mid = (left + right) / 2
        left_arr  = merge_sort_internal(array, left, mid)
        right_arr = merge_sort_internal(array, mid+1, right)
        result = linear_merge(left_arr, right_arr)
        return result

def linear_merge(left_arr, right_arr):
    left_len  = len(left_arr)
    right_len = len(right_arr)
    temp = [None] * (left_len + right_len)
    left_pos = right_pos = temp_pos = 0

    while temp_pos < len(temp):
        if left_pos >= len(left_arr) or (right_pos < len(right_arr) and compare(right_arr[right_pos], left_arr[left_pos])):
            temp[temp_pos] = right_arr[right_pos]
            right_pos += 1
        else:
            temp[temp_pos] = left_arr[left_pos]
            left_pos += 1

        temp_pos += 1

    return temp

def compare(a, b):
    return a < b

def _bsearch_nearest_lower(list:list[int], x:int, low:int, high:int) -> int:
    """
    Description:
        Simple binary search for the nearest number's index in an ascending sequence of unique integers.
        Very specific, so recommend against using it for general scenarios.

    Args:
        list (list[int]): The list of sentences to be compared against.
        x (int): Target number.
        low (int): Search range start.
        high (int): Search range end.

    Returns:
        int: The index of a match or the nearest match of a lower index.

    Examples:
        bsearch_nearest_lower([3, 9, 10, 13, 22], 21, 0, 4) returns 3
        bsearch_nearest_lower([3, 9, 10, 13, 22], 10, 0, 4) returns 2
    """
    while low <= high and high < len(list):    
        mid = low + (high - low)//2

        if list[mid] == x:
            return mid    
        elif list[mid] < x:
            # Check if reached upper end of sequence
            if mid+1 >= len(list):
                return len(list)-1

            if list[mid+1] > x:
                return mid
            elif list[mid+1] == x:
                return mid+1
            else:
                low = mid + 1
        else:
            high = mid - 1

    # If lower than lowest member in sequence, return -1
    return -1

print(_bsearch_nearest_lower([3, 9, 10, 13, 22], 21, 0, 4))
print(_bsearch_nearest_lower([3, 9, 10, 13, 22], 2, 0, 4))
print(_bsearch_nearest_lower([3, 9, 10, 13, 22], 9, 0, 4))
print(_bsearch_nearest_lower([3, 9, 10, 13, 22], 12, 0, 4))
print(_bsearch_nearest_lower([3, 9, 10, 13, 22], 22, 0, 4))
print(_bsearch_nearest_lower([3, 9, 10, 13, 22], 55, 0, 4))

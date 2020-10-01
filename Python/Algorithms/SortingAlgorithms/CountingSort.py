class CountingSort:
    """ CountingSort Algorithm Implementation in Python 3.0+
        arr : Unorded list
        output : Return list in ascending order.
        time complexity : O(n + r) where n is the number of items and
                          r is the range.
        Example :
        >>> sort = CountingSort()
        >>> sort([4, 2, 6, 5, 9, 8], 10)
        [2, 4, 5, 6, 8, 9]
    """

    def __init__(self):
        print("Counting Sort Algorithm is Initialized")

    def __call__(self, arr, max_val=-1):
        if max_val == -1:
            max_val = max(arr)
        m = max_val + 1
        count = [0] * m

        # count frequency
        for a in arr:
            count[a] += 1
        # put elements in arr
        i = 0
        for a in range(m):
            for c in range(count[a]):
                arr[i] = a
                i += 1
        return arr


sort = CountingSort()
print(sort([10, 9, 5, 11, 2], 15))
print(sort([10, 9, 5, 11, 2]))

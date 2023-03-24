from collections import defaultdict


def find_duplicate(nums):

    a = defaultdict(lambda: 0)

    for num in nums:

        if type(num) == str or int(num) < 0:
            return False

        a[num] = a[num] + 1

        if a[num] > 1:
            return num

    return False

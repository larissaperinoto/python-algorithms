from collections import defaultdict


def find_duplicate(nums):

    a = defaultdict(lambda: 0)

    try:
        for num in nums:

            if int(num) < 0:
                raise TypeError

            a[num] = a[num] + 1

            if a[num] > 1:
                return num

        return False
    except (TypeError, ValueError):
        return False


""" def create_dict(a, num):

    if int(num) < 0:
        raise TypeError

    try:
        a[num] = a[num] + 1

    except (KeyError):

        a[num] = 1

    return a
 """

def find_duplicate(nums):

    a = {}

    try:
        for num in nums:
            a.update(create_dict(a, num))

            if a[num] > 1:
                return num

        return False
    except (TypeError, ValueError):
        return False


def create_dict(a, num):

    if int(num) < 0:
        raise TypeError

    try:
        a[num] = a[num] + 1

    except (KeyError):

        a[num] = 1

    return a

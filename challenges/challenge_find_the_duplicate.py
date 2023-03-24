def find_duplicate(nums):

    new = []
    try:
        for num in nums:
            if int(num) < 0:
                raise TypeError
            if num not in new:
                new.append(num)
            else:
               return num
        return False
    except (TypeError, ValueError):
        return False

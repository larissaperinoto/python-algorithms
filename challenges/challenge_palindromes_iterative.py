def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    if word == "".join(reversed(word)):
        return True

    return False

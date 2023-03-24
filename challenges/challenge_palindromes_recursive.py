def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    if low_index >= high_index:
        return True

    if word[low_index] == word[high_index]:
        low_index += 1
        high_index -= 1
        return is_palindrome_recursive(word, low_index, high_index)

    else:
        return False

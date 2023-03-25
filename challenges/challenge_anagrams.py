def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    first = selection_sort(list(first_string.lower()))
    second = selection_sort(list(second_string.lower()))
    f_ordered = ''.join(first)
    s_ordered = ''.join(second)

    return (f_ordered, s_ordered, f_ordered == s_ordered)


def selection_sort(string):
    n = len(string)

    for index in range(n - 1):
        min_element_index = index

        for search_index in range(index + 1, n):
            if string[search_index] < string[min_element_index]:
                min_element_index = search_index

        current_element = string[index]
        string[index] = string[min_element_index]
        string[min_element_index] = current_element

    return string

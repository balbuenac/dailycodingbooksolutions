def is_palindrome_indices(A):
    words = {}
    for i in range(0, len(A)):
        word = A[i]
        words[word] = i

    result = []
    for word in A:
        initial = words[word]
        first_option = word[::-1]
        second_option = first_option[1:]
        print(first_option, second_option)
        if first_option in words:
            i = initial
            j = words[first_option]
            if i != j:
                result.append([i, j ])
        if second_option in words:
            i = initial
            j = words[second_option]
            if i != j:
                result.append([i, j ])
    return result
A = ['code', 'edoc', 'da', 'd']
print(is_palindrome_indices(A))

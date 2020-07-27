
def check_pattern(str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the 'char_frequency' with the current window
    # try to extend the range [window_start, window_end]
    res = []
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            res.append(window_start)

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return res

S = "abxba"
W = "ab"
print(check_pattern(S, W))

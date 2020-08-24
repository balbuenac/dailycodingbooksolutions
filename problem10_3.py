def check_path(start, end, dict):
    if len(end) == 0:
        return True

    for i, c in enumerate(end):
        new_word = list(start)
        new_word[i] = c
        s = "".join(new_word)
        if s in dict:
            new_end = end.replace(c, '')
            return check_path(s, new_end, dict)
    return False
words = ["dog", "dot", "daz", "cat"]
start = "dog"
end = "cat"
dict = {}
for word in words:
    if not word in dict:
        dict[word] = True
print(check_path(start, end, dict))
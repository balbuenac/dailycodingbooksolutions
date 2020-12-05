_end = '_end_'
max_total = 0

def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end
    return root

def max_val(d, total, scores, letters):
    global max_total
    if d is None or d == '_end_':
        print("the total is " + str(total))
        max_total = max(total, max_total)
        return total
    for x,y in d.items():
        score  = 0
        if x != '_end_':
            score = scores[x]
        print(total, score, x, letters)
        if letters and x in letters:
            print('hes')
            max_val(d[x], total + score, scores, letters.remove(x))
        else:
            print('no')
            max_val(d[x], total, scores, letters)
    return 0

scores = {'a':2, 'c':1, 'd':4, 'g':0, 'o':5, 't':1}
print(scores)
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
sorted_words = []
for w in words:
    sorted_words.append(sorted(w))
root = make_trie(sorted_words)

total = 0
max_val(root, total,scores,letters)
print(max_total)
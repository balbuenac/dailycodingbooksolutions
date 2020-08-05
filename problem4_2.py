input = "()[]{}}"
open = "([{"
close = "}])"
brackets = []
i = 0
while i < len(input):
    curr = input[i]
    if curr in open:
        brackets.append(curr)
    elif curr in close:
        if brackets:
            last = brackets.pop()
            if curr == ')' and last != '(':
                break
            elif curr == ']' and last != '[':
                print("Not Balanced")
                break
            elif curr == '}' and last != '{':
                print("Not Balanced")
                break
        else:
            print("Not Balanced")
            break
    i += 1
if len(brackets) > 0:
    print("Not Balanced")
else:
    print("Balanced")

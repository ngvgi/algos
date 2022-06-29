def solution(s):
    if len(s) == 0:
        return True
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    char_array = []

    for i in range(0, len(s)):
        if s[i] in opening:
            char_array.append(s[i])
            continue
        if s[i] in closing:
            if len(char_array) == 0:
                char_array.append(s[i])
                continue
            idx = closing.index(s[i])
            if char_array[-1] == opening[idx]:
                char_array.pop(-1)
                continue
            char_array.append(s[i])

    if len(char_array) > 0:
        return 0
    return 1


print(solution(''))

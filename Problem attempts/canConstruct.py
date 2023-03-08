def canConstruct(targetString, wordbank):
    if targetString == '':
        return True

    for word in wordbank:
        if wordbank.index(word) == 0:
            suffix = targetString[len(word):]
            if canConstruct(suffix, wordbank):
                return True

    return False


print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))

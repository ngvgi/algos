def canConstruct(target, wordbank, memo={}):
    if target == "":
        return True

    if target in memo:
        return memo[target]

    for word in wordbank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct(suffix, wordbank, memo) == True:
                    memo[target] = True
                    return True
        except Exception as e:
            memo[target] = False
            return False


# print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
      'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))

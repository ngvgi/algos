def canConstruct(target, wordbank, memo={}):
    if target == '':
        return True

    for word in wordbank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct(suffix, wordbank, memo) == True:
                    memo[target] = True
                    return True

        except Exception as e:
            pass

    memo[target] = False
    return False


# print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeef', [
      'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))

import string


def has_punc(s, delimiters=[]):
    return (any(d in s for d in delimiters))


def recur_split(s, delimiters=None):
    if delimiters == None:
        delimiters = [punc for punc in string.punctuation]
        delimiters.remove('.')
        delimiters += [' and ']

    s = s.lower()

    if not has_punc(s, delimiters):
        return 1

    count = 0

    for d in delimiters:

        vals = s.split(d)
        if len(vals) == 1:
            continue

        all_same_punc = True

        for val in vals:
            if not has_punc(val, delimiters):
                continue
            all_same_punc = False

        if all_same_punc:
            if '' in vals:
                return len(vals) - 1
            return len(vals)

        count += 1
        s = " ".join(vals)
        delimiters = delimiters.remove(d)
        remaining_count = recur_split(s, delimiters)
        return count + remaining_count


print(recur_split('HASMUKHCHANDRA G SHAH AND OTHERS '))  # 2
print(recur_split('DILIP PREMCHAND AND BINDI SAVLA '))  # 2
print(recur_split('PAUL, JOSEPHINE AND AGNES MULINGE '))  # 3
print(recur_split('BHARAT ,BHAVNA AND SHREENAL ODHAVJI '))  # 3
print(recur_split('STEPHEN G-RUTH G-CONSTANCE F'))  # 3
print(recur_split('JONATHAN N KARANJA, NGUMO M WAMBUI '))  # 2
print(recur_split('MICHAEL ANDERSEN / A P W WACHIRA '))  # 2

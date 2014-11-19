


def fancy_shuffle(s):
    letters = {}
    length = len(s)

    for l in s:
        letters[l] = letters.get(l,0) + 1

    new_s = ''
    new_len = 0

    while new_len < length:
        nl = get_new_letter(new_s, letters)
        if nl:
            new_s += nl
            letters[nl] -= 1
            new_len += 1
        else:
            return False

    return new_s


def get_new_letter(s, letters):
    if len(s) == 0:
        return letters.keys()[0]
    else:
        for l in letters:
            if l != s[-1] and letters[l] > 0:
                return l
        return None

if __name__ == '__main__':
    for s in ['abc', 'abba', 'abab', 'aabc', 'abcaa', 'abcabcabacaa']:
        print "%s: %s" % (s, fancy_shuffle(s))
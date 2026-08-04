def firstUniqueCharacter(s):
    char_c = {}
    for char in s:
        char_c[char] = char_c.get(char, 0) + 1

    for i,num in enumerate(s):
        if char_c[num] == 1:
            return i

    return -1
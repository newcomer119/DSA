# Valid Anagrams

def valid_anagram(s,t):
    if len(s) != len(t):
        return False

    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

    for char in t:
        if char not in freq_map:
            return False

        freq_map[char] -= 1

        if freq_map[char] < 0:
            return False

    return True
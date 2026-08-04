# Find Common Characters 

def common_characters(words):
    freq = {}
    for char in words[0]:
        freq[char] = freq.get(char, 0) + 1

    for char in freq:
        for word in words[1:]:
            freq[char] =min(freq[char], word.count(char))
    res = []
    for char, count in freq.items():
        res.extend([char] * count)

    return res
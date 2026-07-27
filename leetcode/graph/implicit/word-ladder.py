# Word Ladder
# Prereq: BFS on Graph

# Word Ladder is "A puzzle begins with two words, and to solve the puzzle one must find a chain of other words to link the two, in which two adjacent words (that is, words in successive steps) differ by one letter."

# For example: cold → cord → card → ward → warm



# Given a start word, an end word, and a list of dictionary words, determine the minimum number of steps to go from the start word to the end word using only words from the dictionary.

# Input:

# start = "cold"
# end = "warm"
# word_list = ["cold", "gold", "cord", "sold", "card", "ward", "warm", "tard"]
# Output:

# 4
# Explanation: We can go from cold to warm by going through cold → cord → card → ward →


from collections import deque
from string import ascii_letters

def word_ladder(begin: str, end: str, word_list: list[str]) -> int:

    if begin == end:
        return 0
    unvisited_words = set(word_list)

    def get_neighbors(word):
        unvisited_neighbors  = []
        for i in range(len(word)):
            for c in ascii_letters:
                next_word = word[:i] + c + word[i + 1 :]
                if next_word in unvisited_words:
                    unvisited_neighbors.append(next_word)
                    unvisited_words.remove(next_word)

        return unvisited_neighbors
    queue = deque([begin])
    # set begin as visited, now begin's neighbor will not contain itself
    unvisited_words.remove(begin)
    distance = 0
    # if current level is non-empty
    while len(queue) > 0:
        # current level contains n nodes
        n = len(queue)
        distance += 1
        # only visit the nodes in the current level to keep track of distance
        for _ in range(n):
            word = queue.popleft()
            for w in get_neighbors(word):
                if w == end:
                    return distance
                queue.append(w)
    # word ladder not found
    return -1


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("cold", "warm", ["cold", "gold", "cord", "sold", "card", "ward", "warm", "tard"], 4),
        ("hit", "cog", ["hit", "hot", "dot", "dog", "lot", "log", "cog"], 4),
        ("a", "a", ["a"], 0),
    ]
    passed = 0
    for begin, end, words, exp in TESTS:
        got = word_ladder(begin, end, words)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {begin}->{end} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")


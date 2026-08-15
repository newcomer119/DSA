# A bunch of cards is laid out in front of you in a line, where the value of each card ranges from 0 to 10^6. A pair of cards is matching if they have the same number value.

# Given a list of integers cards, your goal is to match a pair of cards, but you can only pick up cards in a consecutive manner. What's the minimum number of cards that you need to pick up to make a pair? If there are no matching pairs, return -1.

# For example, given cards = [3, 4, 2, 3, 4, 7], then picking up [3, 4, 2, 3] makes a pair of 3s and picking up [4, 2, 3, 4] matches two 4s. We need 4 consecutive cards to match a pair of 3s and 4 consecutive cards to match 4s, so you need to pick up at least 4 cards to make a match.

# Try it you


from collections import Counter
def least_consecutive_cards_to_match(cards: list[int]) -> int:
    window = Counter()
    left = 0
    shortest = len(cards) + 1
    for right in range(len(cards)):
        window[cards[right]] += 1
        while window[cards[right]] == 2:
            shortest = min(shortest, right - left + 1)
            window[cards[left]] -= 1
            left += 1
    return shortest if shortest != len(cards) + 1 else -1
        
    # window  = Counter()
    # left = 0
    # shortest = len(cards) + 1

    # for right in range(len(cards)):
    #     window[cards[right]] += 1
    #     while window[cards[right]] == 2:
    #         # we have found a subarray
    #         shortest = min(shortest , right -left + 1)
    #         window[cards[left]] -= 1
    #         left += 1

    # return shortest if shortest != len(cards) + 1 else -1
  

# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([3, 4, 2, 3, 4, 7], 4), ([1, 2, 3, 4], -1), ([1, 1], 2)]
    passed = 0
    for cards, exp in TESTS:
        got = least_consecutive_cards_to_match(cards)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {cards} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
KEYBOARD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
def letter_combinations_of_phone_number(digits: str) -> list[str]:
    res = []
    if not digits:
        return res

    def dfs(start_index,path) -> None:
        if start_index == len(digits):
            res.append("".join(path))
            return 

        next_number = digits[start_index]
        for letter in KEYBOARD[next_number]:
            path.append(letter)
            dfs(start_index + 1,path)
            path.pop()


    dfs(0,[])
    return res
        

    return res


# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(letter_combinations_of_phone_number("23"))
    exp = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] digits='23' -> {len(got)} combos")
    print(f"\n{1 if ok else 0}/1 passed")

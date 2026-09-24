def merge_unique(list1: list[int], list2: list[int]) -> list[int]:
    res = []
    for i in range(len(list1)):
        if list1[i] not in res:
            res.append(list1[i])

    for j in range(len(list2)):
        if list2[j] not in res:
            res.append(list2[j])
    return res


def run_tests():
    tests = [
        {
            "list1": [4, 2, 7, 2],
            "list2": [7, 5, 4, 9],
            "expected": [4, 2, 7, 5, 9]
        },
        {
            "list1": [1, 2, 3],
            "list2": [4, 5, 6],
            "expected": [1, 2, 3, 4, 5, 6]
        },
        {
            "list1": [1, 1, 1],
            "list2": [1, 1],
            "expected": [1]
        },
        {
            "list1": [],
            "list2": [3, 2, 3],
            "expected": [3, 2]
        },
        {
            "list1": [5, 4, 5],
            "list2": [],
            "expected": [5, 4]
        },
        {
            "list1": [],
            "list2": [],
            "expected": []
        }
    ]

    for i, test in enumerate(tests, 1):
        result = merge_unique(test["list1"], test["list2"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  List 1:  ", test["list1"])
            print("  List 2:  ", test["list2"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()
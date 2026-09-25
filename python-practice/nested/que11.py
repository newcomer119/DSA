def common_values(list1: list[int], list2: list[int]) -> list[int]:
    res = []

    for i in range(len(list1)):
        if list1[i] in list2 and list1[i] not in res:
            res.append(list1[i])

    return res

def run_tests():
    tests = [
        {
            "list1": [4, 2, 7, 5],
            "list2": [7, 4, 9, 2],
            "expected": [4, 2, 7]
        },
        {
            "list1": [1, 2, 2, 3, 4],
            "list2": [2, 4, 4, 5],
            "expected": [2, 4]
        },
        {
            "list1": [1, 2, 3],
            "list2": [4, 5, 6],
            "expected": []
        },
        {
            "list1": [],
            "list2": [1, 2],
            "expected": []
        },
        {
            "list1": [5, 5, 5],
            "list2": [5],
            "expected": [5]
        },
        {
            "list1": [-1, 0, 2, -1],
            "list2": [3, -1, 0],
            "expected": [-1, 0]
        }
    ]

    for i, test in enumerate(tests, 1):
        result = common_values(test["list1"], test["list2"])

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
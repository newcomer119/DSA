def compare_interests(user1: list[str], user2: list[str]) -> dict[str, set[str]]:   
    res = {}
    
    set1 = set(user1)
    set2 = set(user2)
    common = set1  & set2 
    only_user1 = set1 - set2
    only_user2 = set2 - set1

    res["common"] = common
    res["only_user1"] = only_user1
    res["only_user2"] = only_user2
    return res

def run_tests():
    tests = [
        {
            "user1": ["Python", "AI", "SQL", "Python"],
            "user2": ["Java", "AI", "Python", "React", "AI"],
            "expected": {
                "common": {"Python", "AI"},
                "only_user1": {"SQL"},
                "only_user2": {"Java", "React"}
            }
        },
        {
            "user1": ["Python", "Java"],
            "user2": ["Python", "Java"],
            "expected": {
                "common": {"Python", "Java"},
                "only_user1": set(),
                "only_user2": set()
            }
        },
        {
            "user1": ["Python"],
            "user2": ["Java"],
            "expected": {
                "common": set(),
                "only_user1": {"Python"},
                "only_user2": {"Java"}
            }
        },
        {
            "user1": [],
            "user2": [],
            "expected": {
                "common": set(),
                "only_user1": set(),
                "only_user2": set()
            }
        }
    ]

    for i, test in enumerate(tests, 1):
        result = compare_interests(
            test["user1"],
            test["user2"]
        )

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()

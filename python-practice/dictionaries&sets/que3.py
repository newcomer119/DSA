def group_by_department(students: list[dict]) -> dict[str, list[str]]:
    res = {}
    for student in students:
        name = student["name"]
        department = student["department"]

        if department not in res:
            res[department] = []
        res[department].append(name)

    return res


def run_tests():
    tests = [
        {
            "input": [
                {"name": "Aman", "department": "CSE"},
                {"name": "Riya", "department": "AI"},
                {"name": "Karan", "department": "CSE"},
                {"name": "Neha", "department": "AI"},
                {"name": "Arjun", "department": "ECE"}
            ],
            "expected": {
                "CSE": ["Aman", "Karan"],
                "AI": ["Riya", "Neha"],
                "ECE": ["Arjun"]
            }
        },
        {
            "input": [
                {"name": "A", "department": "CSE"},
                {"name": "B", "department": "CSE"}
            ],
            "expected": {
                "CSE": ["A", "B"]
            }
        },
        {
            "input": [
                {"name": "A", "department": "AI"},
                {"name": "B", "department": "CSE"},
                {"name": "C", "department": "ECE"}
            ],
            "expected": {
                "AI": ["A"],
                "CSE": ["B"],
                "ECE": ["C"]
            }
        },
        {
            "input": [],
            "expected": {}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = group_by_department(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()

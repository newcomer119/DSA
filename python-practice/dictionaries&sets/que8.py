def group_by_skill(employees: list[dict]) -> dict[str, list[str]]:
    res = {}
    for employee in employees:
        name = employee["name"]
        skills = employee["skills"]
        for skill in skills:
            if skill not in res:
                res[skill] = []

            res[skill].append(name)

    return res

    


def run_tests():
    tests = [
        {
            "input": [
                {"name": "Aman", "skills": ["Python", "SQL"]},
                {"name": "Riya", "skills": ["Java", "Python"]},
                {"name": "Karan", "skills": ["SQL", "React"]},
                {"name": "Neha", "skills": ["Python", "React"]}
            ],
            "expected": {
                "Python": ["Aman", "Riya", "Neha"],
                "SQL": ["Aman", "Karan"],
                "Java": ["Riya"],
                "React": ["Karan", "Neha"]
            }
        },
        {
            "input": [
                {"name": "A", "skills": ["Python"]},
                {"name": "B", "skills": ["Python"]}
            ],
            "expected": {
                "Python": ["A", "B"]
            }
        },
        {
            "input": [
                {"name": "A", "skills": []},
                {"name": "B", "skills": ["Java"]}
            ],
            "expected": {
                "Java": ["B"]
            }
        },
        {
            "input": [],
            "expected": {}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = group_by_skill(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()
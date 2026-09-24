def count_skills(departments: list[list[dict]]) -> dict[str, int]:
    freq = {}
    for department in departments:
        for employee in department:
            skills = employee["skills"]
            for skill in skills:
                freq[skill] = freq.get(skill, 0) + 1

    return freq
            

def run_tests():
    tests = [
        {
            "input": [
                [
                    {"name": "Aman", "skills": ["Python", "SQL"]},
                    {"name": "Riya", "skills": ["Java", "Python"]}
                ],
                [
                    {"name": "Karan", "skills": ["Python", "React", "SQL"]},
                    {"name": "Neha", "skills": ["Java", "React"]}
                ]
            ],
            "expected": {
                "Python": 3,
                "SQL": 2,
                "Java": 2,
                "React": 2
            }
        },
        {
            "input": [
                [
                    {"name": "A", "skills": ["Python"]},
                    {"name": "B", "skills": ["Python", "Java"]}
                ]
            ],
            "expected": {
                "Python": 2,
                "Java": 1
            }
        },
        {
            "input": [
                [],
                [
                    {"name": "A", "skills": ["C++", "Python"]}
                ],
                []
            ],
            "expected": {
                "C++": 1,
                "Python": 1
            }
        },
        {
            "input": [],
            "expected": {}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = count_skills(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()
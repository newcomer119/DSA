def parse_students(records: list[str]) -> list[dict]:
    res = []
    for record in records:
        parts = record.split(",")
        name = parts[0]
        departments = parts[1]
        marks = int(parts[2])

        student = {"name" : name, "department" : departments, "marks" : marks}
        res.append(student)
    return res
            



def run_tests():
    tests = [
        {
            "input": [
                "Aman,CSE,82",
                "Riya,AI,91",
                "Karan,CSE,75"
            ],
            "expected": [
                {"name": "Aman", "department": "CSE", "marks": 82},
                {"name": "Riya", "department": "AI", "marks": 91},
                {"name": "Karan", "department": "CSE", "marks": 75}
            ]
        },
        {
            "input": [
                "John,ECE,100"
            ],
            "expected": [
                {"name": "John", "department": "ECE", "marks": 100}
            ]
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [
                "A,CSE,0",
                "B,AI,50"
            ],
            "expected": [
                {"name": "A", "department": "CSE", "marks": 0},
                {"name": "B", "department": "AI", "marks": 50}
            ]
        }
    ]

    for i, test in enumerate(tests, 1):
        result = parse_students(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("Input:   ", test["input"])
            print("Expected:", test["expected"])
            print("Got:     ", result)


if __name__ == "__main__":
    run_tests()
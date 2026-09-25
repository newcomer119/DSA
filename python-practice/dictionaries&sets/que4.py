def department_averages(students: list[dict]) -> dict[str, float]:
    # total = {}
    # count = {}
    # averages = {}
    # for student in students:
    #     department = student["department"]
    #     marks = student["marks"]

    #     if department not in total:
    #         total[department] = 0
    #         count[department] = 0
    #     total[department] = total[department] + marks
    #     count[department]  = count[department] + 1

    #     for department in total:
    #         averages[department] = total[department] / count[department]
            
    # return averages
    total = {}
    count = {}
    averages = {}

    for student in students:
        department = student["department"]
        marks = student["marks"]

        if department not in total:
            total[department] = 0
            count[department] = 0

        total[department] = total[department] + marks
        count[department] = count[department] + 1

    for department in total:
        averages[department] = total[department] / count[department]

    return averages




def run_tests():
    tests = [
        {
            "input": [
                {"name": "Aman", "department": "CSE", "marks": 80},
                {"name": "Riya", "department": "AI", "marks": 90},
                {"name": "Karan", "department": "CSE", "marks": 70},
                {"name": "Neha", "department": "AI", "marks": 100},
                {"name": "Arjun", "department": "ECE", "marks": 75}
            ],
            "expected": {
                "CSE": 75.0,
                "AI": 95.0,
                "ECE": 75.0
            }
        },
        {
            "input": [
                {"name": "A", "department": "CSE", "marks": 50},
                {"name": "B", "department": "CSE", "marks": 100}
            ],
            "expected": {
                "CSE": 75.0
            }
        },
        {
            "input": [
                {"name": "A", "department": "AI", "marks": 80}
            ],
            "expected": {
                "AI": 80.0
            }
        },
        {
            "input": [],
            "expected": {}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = department_averages(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()
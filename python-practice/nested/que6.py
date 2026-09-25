def build_students(names: list[str], marks: list[int]) -> list[dict]:
    res = []
    for i in range(len(names)):
        student = {"name" : names[i], "marks" : marks[i]}
        res.append(student)
    return res


def run_tests():
    tests = [
        {
            "names": ["Aman", "Riya", "Karan"],
            "marks": [82, 91, 67],
            "expected": [
                {"name": "Aman", "marks": 82},
                {"name": "Riya", "marks": 91},
                {"name": "Karan", "marks": 67}
            ]
        },
        {
            "names": ["A", "B"],
            "marks": [50, 100],
            "expected": [
                {"name": "A", "marks": 50},
                {"name": "B", "marks": 100}
            ]
        },
        {
            "names": ["John"],
            "marks": [75],
            "expected": [
                {"name": "John", "marks": 75}
            ]
        },
        {
            "names": [],
            "marks": [],
            "expected": []
        }
    ]

    for i, test in enumerate(tests, 1):
        result = build_students(test["names"], test["marks"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Names:   ", test["names"])
            print("  Marks:   ", test["marks"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()
# from collections import Counter

# words = ["python", "java", "python", "sql", "java", "python"]

# freq = Counter(words)

# print(freq)
# print(freq["python"])
# print(freq["java"])

# from collections import defaultdict

# groups = defaultdict(list)

# groups["Python"].append("Aman")
# groups["Python"].append("Riya")
# groups["Java"].append("Karan")

# print(groups)


from collections import defaultdict


def group_departments(students: list[dict]) -> dict[str, list[str]]:
    res =  defaultdict(list)

    for student in students:
        name = student["name"]
        department= student["department"]

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
            "input": [],
            "expected": {}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = group_departments(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("Expected:", test["expected"])
            print("Got:     ", result)


if __name__ == "__main__":
    run_tests()
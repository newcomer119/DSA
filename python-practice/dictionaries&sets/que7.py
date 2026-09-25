def filter_employees(employees: list[dict], department: str, minimum_salary: int) -> list[dict]:
    res = []
    for employee in employees:
        depart = employee["department"]
        salary = employee["salary"]

        if depart == department and  salary >= minimum_salary:
            res.append(employee)

    return res


def run_tests():
    tests = [
        {
            "employees": [
                {"name": "Aman", "department": "CSE", "salary": 70000},
                {"name": "Riya", "department": "AI", "salary": 90000},
                {"name": "Karan", "department": "CSE", "salary": 85000},
                {"name": "Neha", "department": "AI", "salary": 65000}
            ],
            "department": "CSE",
            "minimum_salary": 80000,
            "expected": [
                {"name": "Karan", "department": "CSE", "salary": 85000}
            ]
        },
        {
            "employees": [
                {"name": "A", "department": "AI", "salary": 50000},
                {"name": "B", "department": "AI", "salary": 75000},
                {"name": "C", "department": "CSE", "salary": 100000}
            ],
            "department": "AI",
            "minimum_salary": 50000,
            "expected": [
                {"name": "A", "department": "AI", "salary": 50000},
                {"name": "B", "department": "AI", "salary": 75000}
            ]
        },
        {
            "employees": [
                {"name": "A", "department": "ECE", "salary": 40000}
            ],
            "department": "CSE",
            "minimum_salary": 30000,
            "expected": []
        },
        {
            "employees": [],
            "department": "AI",
            "minimum_salary": 50000,
            "expected": []
        }
    ]

    for i, test in enumerate(tests, 1):
        result = filter_employees(
            test["employees"],
            test["department"],
            test["minimum_salary"]
        )

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()

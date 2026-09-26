def parse_data(text: str) -> dict:
    parts = text.split(",")
    return parts


def run_tests():
    tests = [
        {
            "input": "name=Aman;age=22;city=Delhi",
            "expected": {
                "name": "Aman",
                "age": 22,
                "city": "Delhi"
            }
        },
        {
            "input": "product=Laptop;price=50000;stock=8",
            "expected": {
                "product": "Laptop",
                "price": 50000,
                "stock": 8
            }
        },
        {
            "input": "language=Python",
            "expected": {
                "language": "Python"
            }
        },
        {
            "input": "",
            "expected": {}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = parse_data(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("Input:   ", repr(test["input"]))
            print("Expected:", test["expected"])
            print("Got:     ", result)


if __name__ == "__main__":
    run_tests()
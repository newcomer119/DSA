def summarize_transactions(transactions: list[dict]) -> dict[str, dict]:
    res = {}
    for transaction in transactions:
        category = transaction["category"]
        amount = transaction["amount"]

        if category not in res:
            res[category] = {"total" : 0, "count" : 0}
        res[category]["total"] = res[category]["total"] + amount 
        res[category]["count"] = res[category]["count"] + 1  
    return res 
def run_tests():
    tests = [
        {
            "input": [
                {"category": "food", "amount": 200},
                {"category": "travel", "amount": 500},
                {"category": "food", "amount": 150},
                {"category": "shopping", "amount": 1000},
                {"category": "travel", "amount": 300}
            ],
            "expected": {
                "food": {"total": 350, "count": 2},
                "travel": {"total": 800, "count": 2},
                "shopping": {"total": 1000, "count": 1}
            }
        },
        {
            "input": [
                {"category": "food", "amount": 100},
                {"category": "food", "amount": 200}
            ],
            "expected": {
                "food": {"total": 300, "count": 2}
            }
        },
        {
            "input": [
                {"category": "travel", "amount": 500}
            ],
            "expected": {
                "travel": {"total": 500, "count": 1}
            }
        },
        {
            "input": [],
            "expected": {}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = summarize_transactions(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()

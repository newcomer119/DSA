def summarize_sales(sales: list[dict]) -> dict[str, dict]:
    res = {}
    for sale in sales:
        product = sale["product"]
        region = sale["region"]
        amount = sale["amount"]
        if product not in res:
            res[product] = {"total_sales" : 0, "transactions" : 0, "regions" : set()}
        res[product]["total_sales"] = res[product]["total_sales"] + amount
        res[product]["transactions"] = res[product]["transactions"] + 1
        res[product]["regions"].add(region)

    return res




    def run_tests():
        tests = [
            {
                "input": [
                    {"product": "Laptop", "region": "North", "amount": 50000},
                    {"product": "Phone", "region": "South", "amount": 20000},
                    {"product": "Laptop", "region": "South", "amount": 45000},
                    {"product": "Phone", "region": "North", "amount": 25000},
                    {"product": "Laptop", "region": "North", "amount": 55000}
                ],
                "expected": {
                    "Laptop": {
                        "total_sales": 150000,
                        "transactions": 3,
                        "regions": {"North", "South"}
                    },
                    "Phone": {
                        "total_sales": 45000,
                        "transactions": 2,
                        "regions": {"North", "South"}
                    }
                }
            },
            {
                "input": [
                    {"product": "Book", "region": "East", "amount": 500},
                    {"product": "Book", "region": "East", "amount": 700}
                ],
                "expected": {
                    "Book": {
                        "total_sales": 1200,
                        "transactions": 2,
                        "regions": {"East"}
                    }
                }
            },
            {
                "input": [],
                "expected": {}
            }
        ]

        for i, test in enumerate(tests, 1):
            result = summarize_sales(test["input"])

            if result == test["expected"]:
                print(f"Test {i}: PASS")
            else:
                print(f"Test {i}: FAIL")
                print("Expected:", test["expected"])
                print("Got:     ", result)


    if __name__ == "__main__":
        run_tests()
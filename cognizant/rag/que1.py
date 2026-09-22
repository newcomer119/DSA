import re


def preprocess_text(text):
    return " ".join(text.strip().lower().split())



# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        (
            "  Machine   Learning\nUses\tDATA.  ",
            "machine learning uses data."
        ),

        (
            "HELLO WORLD",
            "hello world"
        ),

        (
            "Python     is     GREAT",
            "python is great"
        ),

        (
            "\nDeep\nLearning\n",
            "deep learning"
        ),

        (
            "RAG\tuses\tretrieval",
            "rag uses retrieval"
        ),

        (
            "   artificial intelligence   ",
            "artificial intelligence"
        ),

        (
            "AI, ML, and RAG!",
            "ai, ml, and rag!"
        ),

        (
            "",
            ""
        ),

        (
            "      ",
            ""
        ),

        (
            "Vector\n\nSearch\t\tSystem",
            "vector search system"
        ),
    ]

    passed = 0

    for i, (text, expected) in enumerate(tests, 1):

        result = preprocess_text(text)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(
                f"Test {i}: FAILED\n"
                f"Expected: {repr(expected)}\n"
                f"Got:      {repr(result)}"
            )

    print(f"\nRESULT: {passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
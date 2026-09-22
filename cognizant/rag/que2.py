def chunk_text(text, chunk_size):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        
        chunk = " ".join(words[start : end])
        chunks.append(chunk)

        start += chunk_size
        
    return chunks


# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        (
            "retrieval augmented generation combines search with language models",
            3,
            [
                "retrieval augmented generation",
                "combines search with",
                "language models"
            ]
        ),

        (
            "python is easy to learn",
            2,
            [
                "python is",
                "easy to",
                "learn"
            ]
        ),

        (
            "machine learning uses data",
            4,
            [
                "machine learning uses data"
            ]
        ),

        (
            "one two three four five six",
            1,
            [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six"
            ]
        ),

        (
            "hello world",
            10,
            [
                "hello world"
            ]
        ),

        (
            "",
            3,
            []
        ),

        (
            "vector databases store embeddings efficiently",
            2,
            [
                "vector databases",
                "store embeddings",
                "efficiently"
            ]
        )
    ]

    passed = 0

    for i, (text, chunk_size, expected) in enumerate(tests, 1):

        result = chunk_text(text, chunk_size)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED")
            print("Expected:", expected)
            print("Got:     ", result)

    print(f"\nRESULT: {passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
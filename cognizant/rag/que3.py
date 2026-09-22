def chunk_text_with_overlap(text, chunk_size, overlap):

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("invalid overlap")

    words = text.split()

    chunks = []
    start = 0

    step = chunk_size - overlap

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        # Current chunk already reached the end
        # of the document, so we're finished.
        if end >= len(words):
            break

        start += step

    return chunks


def run_tests():

    tests = [
        (
            "one two three four five six seven eight",
            4,
            1,
            [
                "one two three four",
                "four five six seven",
                "seven eight"
            ]
        ),

        (
            "python machine learning artificial intelligence",
            3,
            1,
            [
                "python machine learning",
                "learning artificial intelligence"
            ]
        ),

        (
            "a b c d e f g",
            3,
            2,
            [
                "a b c",
                "b c d",
                "c d e",
                "d e f",
                "e f g"
            ]
        ),

        # No overlap
        (
            "one two three four five six",
            2,
            0,
            [
                "one two",
                "three four",
                "five six"
            ]
        ),

        # Entire text fits in one chunk
        (
            "hello world",
            5,
            2,
            [
                "hello world"
            ]
        ),

        # Empty document
        (
            "",
            3,
            1,
            []
        ),

        # chunk_size = 1
        (
            "a b c",
            1,
            0,
            [
                "a",
                "b",
                "c"
            ]
        )
    ]

    passed = 0

    for i, (text, chunk_size, overlap, expected) in enumerate(tests, 1):

        result = chunk_text_with_overlap(
            text,
            chunk_size,
            overlap
        )

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

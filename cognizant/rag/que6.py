import numpy as np


def cosine_similarity(a, b):

    A= np.array(a)
    B = np.array(b)

    dot_product = np.dot(A, B)

    norm_a = np.linalg.norm(A)
    norm_b = np.linalg.norm(B)

    if norm_a == 0 or norm_b == 0:
        return 0

    similarity = dot_product / (norm_a * norm_b)

    return similarity


# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        # Identical
        (
            np.array([1.0, 0.0]),
            np.array([1.0, 0.0]),
            1.0
        ),

        # Orthogonal
        (
            np.array([1.0, 0.0]),
            np.array([0.0, 1.0]),
            0.0
        ),

        # Opposite
        (
            np.array([1.0, 0.0]),
            np.array([-1.0, 0.0]),
            -1.0
        ),

        # Same direction, different magnitude
        (
            np.array([1.0, 2.0]),
            np.array([2.0, 4.0]),
            1.0
        ),

        # General case
        (
            np.array([1.0, 1.0]),
            np.array([1.0, 0.0]),
            1 / np.sqrt(2)
        ),

        # Zero vector
        (
            np.array([0.0, 0.0]),
            np.array([1.0, 2.0]),
            0.0
        )
    ]

    passed = 0

    for i, (a, b, expected) in enumerate(tests, 1):

        result = cosine_similarity(a, b)

        if abs(result - expected) < 1e-6:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(
                f"Test {i}: FAILED | "
                f"expected={expected}, got={result}"
            )

    print(f"\nRESULT: {passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
import numpy as np


# =============================================
# MOCK EMBEDDING MODEL
# DO NOT MODIFY
# =============================================

class MockEmbeddingModel:

    def embed(self, texts):

        embeddings = []

        for text in texts:

            length = len(text)
            words = len(text.split())
            vowels = sum(
                1 for char in text.lower()
                if char in "aeiou"
            )

            embeddings.append([
                float(length),
                float(words),
                float(vowels)
            ])

        return np.array(embeddings, dtype=float)


# =============================================
# TODO
# =============================================

def generate_embeddings(chunks, model):

    """
    Generate one embedding for every chunk.

    Requirements:

    1. Use the provided model.
    2. Return a NumPy array.
    3. There must be one embedding per chunk.
    4. If chunks is empty, return an empty
       NumPy array with shape (0, 3).
    """

    # WRITE YOUR SOLUTION HERE
    if not chunks:
        return np.empty((0,3))

    embeddings = model.embed(chunks)

    return embeddings
    



# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    model = MockEmbeddingModel()

    # -----------------------------------------
    # Test 1
    # -----------------------------------------

    chunks = [
        "python programming",
        "machine learning",
        "vector database"
    ]

    embeddings = generate_embeddings(chunks, model)

    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape == (3, 3)

    print("Test 1: PASSED")


    # -----------------------------------------
    # Test 2
    # -----------------------------------------

    chunks = [
        "hello world"
    ]

    embeddings = generate_embeddings(chunks, model)

    assert embeddings.shape == (1, 3)

    print("Test 2: PASSED")


    # -----------------------------------------
    # Test 3
    # -----------------------------------------

    chunks = []

    embeddings = generate_embeddings(chunks, model)

    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape == (0, 3)

    print("Test 3: PASSED")


    # -----------------------------------------
    # Test 4 — values
    # -----------------------------------------

    chunks = ["abc"]

    embeddings = generate_embeddings(chunks, model)

    # "abc"
    # length = 3
    # words  = 1
    # vowels = 1

    expected = np.array([
        [3.0, 1.0, 1.0]
    ])

    assert np.allclose(embeddings, expected)

    print("Test 4: PASSED")


    # -----------------------------------------
    # Test 5 — one embedding per chunk
    # -----------------------------------------

    chunks = [
        "one",
        "two words",
        "three word sentence"
    ]

    embeddings = generate_embeddings(chunks, model)

    assert len(embeddings) == len(chunks)

    print("Test 5: PASSED")


    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    run_tests()
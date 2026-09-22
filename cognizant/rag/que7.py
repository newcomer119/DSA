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
                1
                for char in text.lower()
                if char in "aeiou"
            )

            embeddings.append([
                float(length),
                float(words),
                float(vowels)
            ])

        return np.array(
            embeddings,
            dtype=float
        )


# =============================================
# PROVIDED
# =============================================

def cosine_similarity(a, b):

    A = np.array(a)
    B = np.array(b)

    dot_product = np.dot(A, B)

    norm_a = np.linalg.norm(A)
    norm_b = np.linalg.norm(B)

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)


# =============================================
# TODO
# =============================================

def retrieve_top_k(query, index, model, k):
    """
    Steps:

    1. Generate embedding for query.

    2. Compare query embedding with every
       embedding in index.

    3. Store similarity + chunk index.

    4. Sort from HIGHEST similarity
       to LOWEST similarity.

    5. Return the top k chunks.
    """

    # WRITE YOUR SOLUTION HERE

    query_embedding = model.embed([query])[0]

    scores = []

    for i, doc_embedding in enumerate(index["embeddings"]):

        sim = cosine_similarity(
            query_embedding,
            doc_embedding
        )

        scores.append((sim, i))

    scores.sort(
        key=lambda x: x[0],
        reverse=True
    )

    results = []

    for sim, i in scores[:k]:
        results.append(index["chunks"][i])

    return results


# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    model = MockEmbeddingModel()

    chunks = [
        "python programming",
        "machine learning",
        "vector database",
        "deep learning models",
        "react frontend development"
    ]

    embeddings = model.embed(chunks)

    index = {
        "chunks": chunks,
        "embeddings": embeddings
    }

    # =========================================
    # TEST 1
    # =========================================

    results = retrieve_top_k(
        "python coding",
        index,
        model,
        2
    )

    assert len(results) == 2

    for chunk in results:
        assert chunk in chunks

    print("Test 1: PASSED")

    # =========================================
    # TEST 2
    # k = 1
    # =========================================

    results = retrieve_top_k(
        "machine learning",
        index,
        model,
        1
    )

    assert len(results) == 1

    print("Test 2: PASSED")

    # =========================================
    # TEST 3
    # k larger than number of chunks
    # =========================================

    results = retrieve_top_k(
        "database",
        index,
        model,
        100
    )

    assert len(results) == len(chunks)

    print("Test 3: PASSED")

    # =========================================
    # TEST 4
    # Empty index
    # =========================================

    empty_index = {
        "chunks": [],
        "embeddings": np.empty((0, 3))
    }

    results = retrieve_top_k(
        "hello",
        empty_index,
        model,
        3
    )

    assert results == []

    print("Test 4: PASSED")

    # =========================================
    # TEST 5
    # Correct ranking
    # =========================================

    custom_index = {

        "chunks": [
            "document A",
            "document B",
            "document C"
        ],

        "embeddings": np.array([
            [1.0, 0.0],
            [0.0, 1.0],
            [0.8, 0.2]
        ])
    }

    class CustomModel:

        def embed(self, texts):

            return np.array([
                [1.0, 0.0]
                for _ in texts
            ])

    custom_model = CustomModel()

    results = retrieve_top_k(
        "query",
        custom_index,
        custom_model,
        2
    )

    expected = [
        "document A",
        "document C"
    ]

    assert results == expected

    print("Test 5: PASSED")

    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    run_tests()

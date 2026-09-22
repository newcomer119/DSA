import numpy as np


# =========================================================
# EMBEDDING MODEL — DO NOT MODIFY
# =========================================================

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


# =========================================================
# BUGGY CODE
# =========================================================

def preprocess_text(text):
    return " ".join(text.strip().lower().split())


# =========================================================
# BUGGY CODE
# =========================================================

def chunk_text(text, chunk_size, overlap):

    if chunk_size <= 0:
        raise ValueError("chunk size must be greater ")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("invalid overlap")

    words = text.split()

    chunks = []

    start = 0

    step = chunk_size - overlap

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(
            words[start:end]
        )

        chunks.append(chunk)

        if end >= len(words):
            break

        start += step

    return chunks


# =========================================================
# BUGGY CODE
# =========================================================


# =========================================================
# BUGGY CODE
# =========================================================

def cosine_similarity(a, b):
    A = np.array(a)
    B = np.array(b)
    dot_product = np.dot(A, B)

    norm_a = np.linalg.norm(A)
    norm_b = np.linalg.norm(B)

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot_product / (norm_a * norm_b)


# =========================================================
# BUGGY CODE
# =========================================================
def create_index(chunks, model):

    if not chunks:
        return {
            "chunks": [],
            "embeddings": np.empty((0, 3))
        }

    embeddings = model.embed(chunks)

    return {
        "chunks": chunks,
        "embeddings": embeddings
    }


def retrieve(query, index, model, k=2):

    query_embedding = model.embed([query])[0]

    scores = []

    for i, embedding in enumerate(index["embeddings"]):

        similarity = cosine_similarity(
            query_embedding,
            embedding
        )

        scores.append((similarity, i))

    scores.sort(
        key=lambda x: x[0],
        reverse=True
    )

    results = []

    for similarity, i in scores[:k]:
        results.append(index["chunks"][i])

    return results


# =========================================================
# PIPELINE — DO NOT MODIFY
# =========================================================

def build_index(
    document,
    model,
    chunk_size=4,
    overlap=1
):

    cleaned = preprocess_text(document)

    chunks = chunk_text(
        cleaned,
        chunk_size,
        overlap
    )

    return create_index(
        chunks,
        model
    )


# =========================================================
# TEST ENVIRONMENT — DO NOT MODIFY
# =========================================================

def run_tests():

    model = MockEmbeddingModel()

    # -----------------------------------------------------
    # TEST 1 — preprocessing
    # -----------------------------------------------------

    result = preprocess_text(
        "  Machine   Learning\nUses\tDATA. "
    )

    expected = (
        "machine learning uses data."
    )

    assert result == expected

    print("Test 1: PASSED")

    # -----------------------------------------------------
    # TEST 2 — chunking
    # -----------------------------------------------------

    result = chunk_text(
        "one two three four five six",
        3,
        1
    )

    expected = [
        "one two three",
        "three four five",
        "five six"
    ]

    assert result == expected

    print("Test 2: PASSED")

    # -----------------------------------------------------
    # TEST 3 — embedding dimensions
    # -----------------------------------------------------

    chunks = [
        "python programming",
        "machine learning",
        "vector database"
    ]

    index = create_index(
        chunks,
        model
    )

    assert (
        index["embeddings"].shape
        ==
        (3, 3)
    )

    print("Test 3: PASSED")

    # -----------------------------------------------------
    # TEST 4 — index alignment
    # -----------------------------------------------------

    assert (
        len(index["chunks"])
        ==
        len(index["embeddings"])
    )

    print("Test 4: PASSED")

    # -----------------------------------------------------
    # TEST 5 — cosine identical
    # -----------------------------------------------------

    result = cosine_similarity(
        np.array([1.0, 0.0]),
        np.array([1.0, 0.0])
    )

    assert abs(result - 1.0) < 1e-6

    print("Test 5: PASSED")

    # -----------------------------------------------------
    # TEST 6 — zero vector
    # -----------------------------------------------------

    result = cosine_similarity(
        np.array([0.0, 0.0]),
        np.array([1.0, 1.0])
    )

    assert result == 0.0

    print("Test 6: PASSED")

    # -----------------------------------------------------
    # TEST 7 — retrieval
    # -----------------------------------------------------

    results = retrieve(
        "python coding",
        index,
        model,
        k=2
    )

    assert len(results) == 2

    for result in results:
        assert result in chunks

    print("Test 7: PASSED")

    # -----------------------------------------------------
    # TEST 8 — deterministic ranking
    # -----------------------------------------------------

    custom_index = {

        "chunks": [
            "A",
            "B",
            "C"
        ],

        "embeddings": np.array([
            [1.0, 0.0],
            [0.0, 1.0],
            [0.8, 0.2]
        ])
    }

    class QueryModel:

        def embed(self, texts):

            return np.array([
                [1.0, 0.0]
                for _ in texts
            ])

    results = retrieve(
        "query",
        custom_index,
        QueryModel(),
        k=2
    )

    assert results == [
        "A",
        "C"
    ]

    print("Test 8: PASSED")

    # -----------------------------------------------------
    # TEST 9 — empty document
    # -----------------------------------------------------

    empty_index = build_index(
        "",
        model
    )

    assert empty_index["chunks"] == []

    assert (
        empty_index["embeddings"].shape
        ==
        (0, 3)
    )

    print("Test 9: PASSED")

    print(
        "\nALL DEBUGGING TESTS PASSED"
    )


if __name__ == "__main__":
    run_tests()

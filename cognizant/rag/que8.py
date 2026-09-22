import numpy as np


# =========================================================
# MOCK EMBEDDING MODEL
# DO NOT MODIFY
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

        return np.array(embeddings, dtype=float)


# =========================================================
# TODO 1 — PREPROCESS
# =========================================================

def preprocess_text(text):
    return " ".join(text.strip().lower().split())
    """
    Requirements:

    - lowercase
    - normalize whitespace
    - remove leading/trailing whitespace

    Punctuation does NOT need to be removed.
    """

# =========================================================
# TODO 2 — CHUNK WITH OVERLAP
# =========================================================


def chunk_text(text, chunk_size, overlap):
    """
    chunk_size and overlap represent WORD counts.

    Requirements:

    - chunk_size > 0
    - 0 <= overlap < chunk_size
    - don't generate redundant trailing chunks

    Example:

    text:
    "one two three four five six"

    chunk_size = 3
    overlap = 1

    result:

    [
        "one two three",
        "three four five",
        "five six"
    ]
    """
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
        chunk = " ".join(words[start: end])

        chunks.append(chunk)

        if end >= len(words):
            break

        start += step

    return chunks


# =========================================================
# TODO 3 — CREATE INDEX
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


def cosine_similarity(a, b):

    A = np.array(a)
    B = np.array(b)

    a_norm = np.linalg.norm(A)
    b_norm = np.linalg.norm(B)

    if a_norm == 0 or b_norm == 0:
        return 0.0

    dot_product = np.dot(A, B)

    return dot_product / (a_norm * b_norm)


def retrieve(query, index, model, k=2):

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


# =========================================================
# COMPLETE PIPELINE
# DO NOT MODIFY
# =========================================================

def build_rag_index(
    document,
    model,
    chunk_size=5,
    overlap=1
):

    cleaned = preprocess_text(document)

    chunks = chunk_text(
        cleaned,
        chunk_size,
        overlap
    )

    index = create_index(
        chunks,
        model
    )

    return index


# =========================================================
# TEST ENVIRONMENT
# =========================================================

def run_tests():

    model = MockEmbeddingModel()

    document = """
        Python is a programming language.

        Machine learning allows computers
        to learn from data.

        Retrieval augmented generation uses
        external documents to provide context
        to language models.

        Vector databases store embeddings
        for efficient similarity search.
    """

    # =====================================================
    # TEST 1 — preprocessing
    # =====================================================

    cleaned = preprocess_text(
        "  Machine   Learning\nUses\tDATA. "
    )

    assert cleaned == "machine learning uses data."

    print("Test 1: PASSED")

    # =====================================================
    # TEST 2 — chunking
    # =====================================================

    chunks = chunk_text(
        "one two three four five six",
        3,
        1
    )

    expected = [
        "one two three",
        "three four five",
        "five six"
    ]

    assert chunks == expected

    print("Test 2: PASSED")

    # =====================================================
    # TEST 3 — build index
    # =====================================================

    index = build_rag_index(
        document,
        model,
        chunk_size=6,
        overlap=2
    )

    assert isinstance(index, dict)

    assert "chunks" in index
    assert "embeddings" in index

    assert len(index["chunks"]) > 0

    assert (
        len(index["chunks"])
        ==
        len(index["embeddings"])
    )

    print("Test 3: PASSED")

    # =====================================================
    # TEST 4 — embedding dimensions
    # =====================================================

    assert index["embeddings"].ndim == 2

    assert index["embeddings"].shape[1] == 3

    print("Test 4: PASSED")

    # =====================================================
    # TEST 5 — cosine similarity
    # =====================================================

    a = np.array([1.0, 0.0])
    b = np.array([1.0, 0.0])

    assert (
        abs(cosine_similarity(a, b) - 1.0)
        < 1e-6
    )

    print("Test 5: PASSED")

    # =====================================================
    # TEST 6 — zero vector
    # =====================================================

    a = np.array([0.0, 0.0])
    b = np.array([1.0, 1.0])

    assert cosine_similarity(a, b) == 0.0

    print("Test 6: PASSED")

    # =====================================================
    # TEST 7 — retrieval count
    # =====================================================

    results = retrieve(
        "python programming",
        index,
        model,
        k=2
    )

    assert len(results) == 2

    for result in results:
        assert result in index["chunks"]

    print("Test 7: PASSED")

    # =====================================================
    # TEST 8 — k > documents
    # =====================================================

    results = retrieve(
        "machine learning",
        index,
        model,
        k=100
    )

    assert len(results) == len(index["chunks"])

    print("Test 8: PASSED")

    # =====================================================
    # TEST 9 — empty document
    # =====================================================

    empty_index = build_rag_index(
        "",
        model,
        chunk_size=5,
        overlap=1
    )

    assert empty_index["chunks"] == []

    assert empty_index["embeddings"].shape == (0, 3)

    assert retrieve(
        "anything",
        empty_index,
        model,
        k=3
    ) == []

    print("Test 9: PASSED")

    # =====================================================
    # TEST 10 — custom retrieval ranking
    # =====================================================

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

    assert results == ["A", "C"]

    print("Test 10: PASSED")

    print("\nALL RAG PIPELINE TESTS PASSED")


if __name__ == "__main__":
    run_tests()

import numpy as np


def create_vector_index(chunks, embeddings):
    if not isinstance(embeddings, np.ndarray):
        raise TypeError("embeddings must be a NumPy array")

    if len(chunks) != len(embeddings):
        raise ValueError("Embedding are required")
    
    return  {
        "chunks" : chunks,
        "embeddings" : embeddings
    }



def run_tests():

    # -----------------------------------------
    # Test 1 — normal index
    # -----------------------------------------

    chunks = [
        "python programming",
        "machine learning",
        "vector databases"
    ]

    embeddings = np.array([
        [10.0, 2.0, 3.0],
        [12.0, 2.0, 5.0],
        [15.0, 2.0, 6.0]
    ])

    index = create_vector_index(
        chunks,
        embeddings
    )

    assert "chunks" in index
    assert "embeddings" in index

    assert len(index["chunks"]) == 3
    assert index["embeddings"].shape == (3, 3)

    print("Test 1: PASSED")


    # -----------------------------------------
    # Test 2 — data preserved
    # -----------------------------------------

    assert index["chunks"][0] == "python programming"

    assert np.array_equal(
        index["embeddings"][0],
        np.array([10.0, 2.0, 3.0])
    )

    print("Test 2: PASSED")


    # -----------------------------------------
    # Test 3 — single chunk
    # -----------------------------------------

    chunks = ["hello world"]

    embeddings = np.array([
        [5.0, 2.0, 1.0]
    ])

    index = create_vector_index(
        chunks,
        embeddings
    )

    assert len(index["chunks"]) == 1
    assert index["embeddings"].shape == (1, 3)

    print("Test 3: PASSED")


    # -----------------------------------------
    # Test 4 — empty index
    # -----------------------------------------

    chunks = []

    embeddings = np.empty((0, 3))

    index = create_vector_index(
        chunks,
        embeddings
    )

    assert index["chunks"] == []
    assert index["embeddings"].shape == (0, 3)

    print("Test 4: PASSED")


    # -----------------------------------------
    # Test 5 — mismatch should fail
    # -----------------------------------------

    chunks = [
        "chunk one",
        "chunk two"
    ]

    embeddings = np.array([
        [1.0, 2.0, 3.0]
    ])

    try:
        create_vector_index(
            chunks,
            embeddings
        )

        print(
            "Test 5: FAILED "
            "(ValueError expected)"
        )

    except ValueError:
        print("Test 5: PASSED")


    # -----------------------------------------
    # Test 6 — embeddings must be numpy
    # -----------------------------------------

    try:
        create_vector_index(
            ["hello"],
            [[1.0, 2.0, 3.0]]
        )

        print(
            "Test 6: FAILED "
            "(TypeError expected)"
        )

    except TypeError:
        print("Test 6: PASSED")


    print("\nTESTING COMPLETE")


if __name__ == "__main__":
    run_tests()
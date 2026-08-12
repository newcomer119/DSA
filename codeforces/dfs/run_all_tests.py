"""
Daily DFS practice checker.

Run all tests:
    python run_all_tests.py

Run one subfolder:
    python run_all_tests.py bst
    python run_all_tests.py advanced

Run one problem:
    python run_all_tests.py invert
    python run_all_tests.py lca
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(relative_path: str):
    path = ROOT / relative_path
    name = path.stem.replace(" ", "_").replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_tree(tokens, node_cls, converter=str):
    """Build tree from preorder tokens; 'x' means null."""
    it = iter(tokens)

    def helper():
        val = next(it)
        if val == "x":
            return None
        left = helper()
        right = helper()
        v = converter(val) if converter is not str else val
        if converter is int:
            v = int(val)
        return node_cls(v, left, right)

    return helper()


def format_tree(node):
    if node is None:
        return ["x"]
    return [str(node.val)] + format_tree(node.left) + format_tree(node.right)


def tree_key(node):
    return " ".join(format_tree(node))


def find_node(root, target):
    if not root:
        return None
    if root.val == target:
        return root
    return find_node(root.left, target) or find_node(root.right, target)


def run_case(name: str, actual, expected) -> bool:
    ok = actual == expected
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        print(f"         expected: {expected!r}")
        print(f"         got:      {actual!r}")
    return ok


def test_invert_binary_tree() -> tuple[int, int]:
    mod = load_module("invert_binary_tree.py")
    tests = [
        (["1", "2", "x", "x", "3", "x", "x"], ["1", "3", "x", "x", "2", "x", "x"]),
        (["x"], ["x"]),
        (["1", "x", "x"], ["1", "x", "x"]),
        (["1", "2", "3", "x", "x", "4", "x", "x", "x", "x", "5", "x", "x"], None),
    ]
    passed = 0
    for tokens, expected in tests:
        root = build_tree(tokens, mod.Node, int)
        got = mod.invert_binary_tree(root)
        if expected is None:
            # just verify invert twice restores structure
            back = mod.invert_binary_tree(got)
            ok = tree_key(back) == tree_key(build_tree(tokens, mod.Node, int))
            name = "double invert restores tree"
        else:
            ok = tree_key(got) == " ".join(expected)
            name = f"invert {tokens[0]}"
        if run_case(name, ok, True):
            passed += 1
    return passed, len(tests)


def test_subtree_of_another() -> tuple[int, int]:
    mod = load_module("subtree_of_another.py")
    tests = [
        (["1", "2", "x", "x", "3", "x", "x"], ["2", "x", "x"], True),
        (["1", "2", "x", "x", "3", "x", "x"], ["3", "x", "x"], True),
        (["1", "2", "x", "x", "3", "x", "x"], ["4", "x", "x"], False),
        (["1", "x", "x"], ["1", "x", "x"], True),
        (["1", "x", "x"], ["x"], True),
    ]
    passed = 0
    for root_t, sub_t, expected in tests:
        root = build_tree(root_t, mod.Node, int)
        sub = build_tree(sub_t, mod.Node, int)
        if run_case(f"root={root_t[0]}, sub={sub_t[0]}", mod.subtree_of_another_tree(root, sub), expected):
            passed += 1
    return passed, len(tests)


def test_balanced_binary_tree() -> tuple[int, int]:
    mod = load_module("balanced_binary_tree.py")
    tests = [
        (["1", "2", "x", "x", "3", "x", "x"], True),
        (["1", "2", "x", "x", "x", "x", "x"], True),
        (["1", "2", "3", "4", "x", "x", "x", "x", "x", "x"], False),
        (["x"], True),
    ]
    passed = 0
    for tokens, expected in tests:
        tree = build_tree(tokens, mod.Node, int)
        if run_case(" ".join(tokens[:3]), mod.is_balanced(tree), expected):
            passed += 1
    return passed, len(tests)


def test_max_depth() -> tuple[int, int]:
    mod = load_module("max_depth.py")
    tests = [
        (["x"], 0),
        (["1", "x", "x"], 0),
        (["1", "2", "x", "x", "3", "x", "x"], 1),
        (["1", "2", "3", "x", "x", "x", "x"], 2),
        (["1", "2", "x", "x", "x", "x", "x"], 1),
    ]
    passed = 0
    for tokens, expected in tests:
        tree = build_tree(tokens, mod.Node, int)
        if run_case(" ".join(tokens[:3]), mod.tree_max_depth(tree), expected):
            passed += 1
    return passed, len(tests)


def test_valid_bst() -> tuple[int, int]:
    mod = load_module("bst/valid_bst.py")
    tests = [
        (["2", "1", "x", "x", "3", "x", "x"], True),
        (["5", "1", "x", "x", "4", "x", "x"], False),
        (["1", "x", "x"], True),
        (["10", "5", "15", "x", "x", "6", "x", "x", "x", "x"], False),
    ]
    passed = 0
    for tokens, expected in tests:
        tree = build_tree(tokens, mod.Node, int)
        if run_case(" ".join(tokens[:3]), mod.valid_bst(tree), expected):
            passed += 1
    return passed, len(tests)


def test_insert_into_bst() -> tuple[int, int]:
    mod = load_module("bst/insert_into_bst.py")
    tests = [
        (["2", "1", "x", "x", "3", "x", "x"], 4, "2 1 x x 3 x 4 x x"),
        (["4", "2", "1", "x", "x", "3", "x", "x", "7", "x", "x"], 5, "4 2 1 x x 3 x x 7 5 x x x"),
        (["x"], 1, "1 x x"),
    ]
    passed = 0
    for tokens, val, expected in tests:
        tree = build_tree(tokens, mod.Node, int)
        got = mod.insert_bst(tree, val)
        if run_case(f"insert {val}", " ".join(format_tree(got)), expected):
            passed += 1
    return passed, len(tests)


def test_lca_of_bst() -> tuple[int, int]:
    mod = load_module("bst/lca_of_bst.py")
    tokens = ["6", "2", "1", "x", "x", "4", "3", "x", "x", "5", "x", "x", "8", "7", "x", "x", "9", "x", "x"]
    tree = build_tree(tokens, mod.Node, int)
    tests = [(2, 8, 6), (2, 4, 2), (3, 5, 4), (1, 3, 2)]
    passed = 0
    for p, q, expected in tests:
        if run_case(f"LCA({p},{q})", mod.lca_on_bst(tree, p, q), expected):
            passed += 1
    return passed, len(tests)


def test_reconstruct_binary_tree() -> tuple[int, int]:
    mod = load_module("advanced/reconstruct_binary_tree.py")
    tests = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], "3 9 x x 20 15 x x 7 x x"),
        ([1, 2, 3], [2, 1, 3], "1 2 x x 3 x x"),
        ([1], [1], "1 x x"),
    ]
    passed = 0
    for preorder, inorder, expected in tests:
        got = mod.construct_binary_tree(preorder, inorder)
        if run_case(f"pre={preorder}", " ".join(format_tree(got)), expected):
            passed += 1
    return passed, len(tests)


def test_serialize_deserialize() -> tuple[int, int]:
    mod = load_module("advanced/SerializingandDeserializingBinaryTree.py")
    tests = [
        ["1", "2", "x", "x", "3", "x", "x"],
        ["1", "x", "x"],
        ["5", "1", "4", "x", "x", "x", "6", "x", "x", "x", "x"],
    ]
    passed = 0
    for tokens in tests:
        original = build_tree(tokens, mod.Node, int)
        serialized = mod.serialize(original)
        restored = mod.deserialize(serialized)
        ok = tree_key(restored) == tree_key(original)
        if run_case(f"round-trip {tokens[0]}", ok, True):
            passed += 1
    return passed, len(tests)


def test_lowest_common_ancestor() -> tuple[int, int]:
    mod = load_module("advanced/Lowest_common_ancestor.py")
    tokens = ["3", "5", "6", "x", "x", "2", "7", "x", "x", "4", "x", "x", "1", "0", "x", "x", "8", "x", "x"]
    tree = build_tree(tokens, mod.Node, int)
    tests = [(5, 1, 3), (5, 4, 5), (6, 4, 5), (6, 7, 5)]
    passed = 0
    for v1, v2, expected in tests:
        n1 = find_node(tree, v1)
        n2 = find_node(tree, v2)
        got = mod.lca(tree, n1, n2)
        if run_case(f"LCA({v1},{v2})", got.val if got else None, expected):
            passed += 1
    return passed, len(tests)


ALL_TESTS = {
    "invert": ("root", test_invert_binary_tree),
    "subtree": ("root", test_subtree_of_another),
    "balanced": ("root", test_balanced_binary_tree),
    "max-depth": ("root", test_max_depth),
    "valid-bst": ("bst", test_valid_bst),
    "insert-bst": ("bst", test_insert_into_bst),
    "lca-bst": ("bst", test_lca_of_bst),
    "reconstruct": ("advanced", test_reconstruct_binary_tree),
    "serialize": ("advanced", test_serialize_deserialize),
    "lca": ("advanced", test_lowest_common_ancestor),
}


def main() -> int:
    filters = [a.lower() for a in sys.argv[1:]]

    if filters:
        selected = {
            k: v for k, v in ALL_TESTS.items()
            if any(f in k or f in v[0] for f in filters)
        }
        if not selected:
            print("No matching problems. Available:")
            for key, (folder, _) in ALL_TESTS.items():
                print(f"  - {key} ({folder})")
            return 1
    else:
        selected = ALL_TESTS

    total_passed = 0
    total_cases = 0
    failed = []
    current_folder = None

    print("=" * 60)
    print("DFS Daily Tests")
    print("=" * 60)

    for key, (folder, runner) in selected.items():
        if folder != current_folder:
            print(f"\n[{folder}]")
            current_folder = folder
        print(f"\n{key}")
        print("-" * len(key))
        passed, count = runner()
        total_passed += passed
        total_cases += count
        if passed != count:
            failed.append(key)

    print("\n" + "=" * 60)
    print(f"Summary: {total_passed}/{total_cases} passed")
    if failed:
        print("Needs review:", ", ".join(failed))
        return 1
    print("All tests passed!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

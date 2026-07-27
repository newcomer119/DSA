"""
Daily BFS practice checker.

Run all tests:
    python run_all_tests.py

Run one problem:
    python run_all_tests.py level-order
    python run_all_tests.py zigzag
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(filename: str):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_tree(tokens, node_cls):
    it = iter(tokens)

    def helper():
        val = next(it)
        if val == "x":
            return None
        return node_cls(int(val), helper(), helper())

    return helper()


def run_case(name: str, actual, expected) -> bool:
    ok = actual == expected
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        print(f"         expected: {expected!r}")
        print(f"         got:      {actual!r}")
    return ok


def test_level_order() -> tuple[int, int]:
    mod = load_module("binary_tree_level_order.py")
    tests = [
        ("empty", ["x"], []),
        ("single node", ["1", "x", "x"], [[1]]),
        ("example tree", ["3", "9", "x", "x", "20", "15", "x", "x", "7", "x", "x"], [[3], [9, 20], [15, 7]]),
        ("complete small", ["1", "2", "x", "x", "3", "x", "x"], [[1], [2, 3]]),
    ]
    passed = 0
    for name, tokens, expected in tests:
        root = build_tree(tokens, mod.Node)
        if run_case(name, mod.level_order_traversal(root), expected):
            passed += 1
    return passed, len(tests)


def test_min_depth() -> tuple[int, int]:
    mod = load_module("binary_tree_min_depth.py")
    tests = [
        ("single node", ["1", "x", "x"], 0),
        ("two levels", ["1", "2", "x", "x", "x", "x", "x"], 1),
        ("deeper on one side", ["1", "2", "x", "x", "3", "x", "x"], 1),
        ("skew left", ["1", "x", "2", "x", "3", "x", "4", "x", "x", "x", "x"], 3),
    ]
    passed = 0
    for name, tokens, expected in tests:
        root = build_tree(tokens, mod.Node)
        if run_case(name, mod.binary_tree_min_depth(root), expected):
            passed += 1
    return passed, len(tests)


def test_right_side_view() -> tuple[int, int]:
    mod = load_module("binary_tree_right_side.py")
    tests = [
        ("single node", ["1", "x", "x"], [1]),
        ("example", ["1", "2", "x", "5", "x", "x", "3", "x", "4", "x", "x"], [1, 3, 4]),
        ("left only chain", ["1", "x", "2", "x", "3", "x", "x"], [1, 2, 3]),
        ("balanced", ["1", "2", "x", "x", "3", "x", "x"], [1, 3]),
    ]
    passed = 0
    for name, tokens, expected in tests:
        root = build_tree(tokens, mod.Node)
        if run_case(name, mod.binary_tree_right_side_view(root), expected):
            passed += 1
    return passed, len(tests)


def test_zigzag() -> tuple[int, int]:
    mod = load_module("binary_tree_zigzag_traversal.py")
    tests = [
        ("single node", ["1", "x", "x"], [[1]]),
        ("example", ["3", "9", "x", "x", "20", "15", "x", "x", "7", "x", "x"], [[3], [20, 9], [15, 7]]),
        ("two levels", ["1", "2", "x", "x", "3", "x", "x"], [[1], [3, 2]]),
        ("empty", ["x"], []),
    ]
    passed = 0
    for name, tokens, expected in tests:
        root = build_tree(tokens, mod.Node)
        if run_case(name, mod.zig_zag_traversal(root), expected):
            passed += 1
    return passed, len(tests)


ALL_TESTS = {
    "level-order": test_level_order,
    "min-depth": test_min_depth,
    "right-side": test_right_side_view,
    "zigzag": test_zigzag,
}


def main() -> int:
    filters = [a.lower() for a in sys.argv[1:]]

    if filters:
        selected = {k: v for k, v in ALL_TESTS.items() if any(f in k for f in filters)}
        if not selected:
            print("Available:", ", ".join(ALL_TESTS))
            return 1
    else:
        selected = ALL_TESTS

    total_passed = 0
    total_cases = 0
    failed = []

    print("=" * 60)
    print("BFS Daily Tests")
    print("=" * 60)

    for key, runner in selected.items():
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

"""
Daily greedy practice checker.

Run all tests:
    python run_all_tests.py

Run one subfolder:
    python run_all_tests.py intervals
    python run_all_tests.py greedy-heap

Run one problem:
    python run_all_tests.py jump-game
    python run_all_tests.py task-scheduler
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


def run_case(name: str, actual, expected) -> bool:
    ok = actual == expected
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        print(f"         expected: {expected!r}")
        print(f"         got:      {actual!r}")
    return ok


def test_jump_game() -> tuple[int, int]:
    mod = load_module("jump-game.py")
    tests = [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False)]
    passed = sum(run_case(str(nums), mod.can_jump(nums), exp) for nums, exp in tests)
    return passed, len(tests)


def test_jump_game_ii() -> tuple[int, int]:
    mod = load_module("jump-game-2.py")
    tests = [([2, 3, 1, 1, 4], 2), ([2, 3, 0, 1, 4], 2)]
    passed = sum(run_case(str(nums), mod.jump(nums), exp) for nums, exp in tests)
    return passed, len(tests)


def test_gas_station() -> tuple[int, int]:
    mod = load_module("gas-stations.py")
    tests = [([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3), ([2, 3, 4], [3, 4, 3], -1)]
    passed = sum(run_case("circuit", mod.can_complete_circuit(gas, cost), exp) for gas, cost, exp in tests)
    return passed, len(tests)


def test_partition_labels() -> tuple[int, int]:
    mod = load_module("partition-label-string.py")
    tests = [("ababcbacadefegdehijhklij", [9, 7, 8]), ("eccbbbbdec", [10])]
    passed = sum(run_case(s[:6], mod.partition_labels(s), exp) for s, exp in tests)
    return passed, len(tests)


def test_merge_intervals() -> tuple[int, int]:
    mod = load_module("intervals/merge-intervals.py")
    tests = [([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])]
    passed = sum(run_case("merge", mod.merge(intervals), exp) for intervals, exp in tests)
    return passed, len(tests)


def test_insert_interval() -> tuple[int, int]:
    mod = load_module("intervals/insert-intervals.py")
    tests = [([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])]
    passed = sum(run_case("insert", mod.insert(intervals, new_iv), exp) for intervals, new_iv, exp in tests)
    return passed, len(tests)


def test_min_arrows() -> tuple[int, int]:
    mod = load_module("intervals/minarrowsburstballoons.py")
    tests = [([[10, 16], [2, 8], [1, 6], [7, 12]], 2), ([[1, 2], [2, 3], [3, 4], [4, 5]], 2)]
    passed = sum(run_case("arrows", mod.find_min_arrow_shots(points), exp) for points, exp in tests)
    return passed, len(tests)


def test_erase_overlap() -> tuple[int, int]:
    mod = load_module("intervals/eraseOevrlapIntervals.py")
    tests = [([[1, 2], [2, 3], [3, 4], [1, 3]], 1), ([[1, 2], [2, 3]], 0)]
    passed = sum(run_case("erase", mod.erase_overlap_intervals(intervals), exp) for intervals, exp in tests)
    return passed, len(tests)


def test_meeting_rooms() -> tuple[int, int]:
    mod = load_module("greedy-heap/meeting-rooms-2.py")
    tests = [([[0, 30], [5, 10], [15, 20]], 2), ([[7, 10], [2, 4]], 1)]
    passed = sum(run_case("rooms", mod.min_meeting_rooms(intervals), exp) for intervals, exp in tests)
    return passed, len(tests)


def test_task_scheduler() -> tuple[int, int]:
    mod = load_module("greedy-heap/task-scheduler.py")
    tests = [(["A", "A", "A", "B", "B", "B"], 2, 8), (["A", "C", "A", "B", "D", "B"], 1, 6)]
    passed = sum(run_case(f"n={n}", mod.least_interval(tasks, n), exp) for tasks, n, exp in tests)
    return passed, len(tests)


def test_ipo() -> tuple[int, int]:
    mod = load_module("greedy-heap/IPO.py")
    tests = [(2, 0, [1, 2, 3], [0, 1, 1], 4), (3, 0, [1, 2, 3], [0, 1, 2], 6)]
    passed = sum(
        run_case(f"k={k}", mod.find_maximized_capital(k, w, profits, cap), exp)
        for k, w, profits, cap, exp in tests
    )
    return passed, len(tests)


ALL_TESTS = {
    "jump-game": ("root", test_jump_game),
    "jump-game-ii": ("root", test_jump_game_ii),
    "gas-station": ("root", test_gas_station),
    "partition-labels": ("root", test_partition_labels),
    "merge-intervals": ("intervals", test_merge_intervals),
    "insert-interval": ("intervals", test_insert_interval),
    "min-arrows": ("intervals", test_min_arrows),
    "erase-overlap": ("intervals", test_erase_overlap),
    "meeting-rooms": ("greedy-heap", test_meeting_rooms),
    "task-scheduler": ("greedy-heap", test_task_scheduler),
    "ipo": ("greedy-heap", test_ipo),
}


def main() -> None:
    selected = sys.argv[1:] if len(sys.argv) > 1 else list(ALL_TESTS)
    total_passed = 0
    total_cases = 0
    current_folder = None

    print("=" * 60)
    print("Greedy Daily Tests")
    print("=" * 60)

    for alias in selected:
        if alias in ("intervals", "greedy-heap"):
            for name, (folder, fn) in ALL_TESTS.items():
                if folder == alias:
                    if current_folder != folder:
                        current_folder = folder
                        print(f"\n[{folder}]")
                    print(f"\n{name}")
                    print("-" * len(name))
                    passed, cases = fn()
                    total_passed += passed
                    total_cases += cases
            continue

        if alias not in ALL_TESTS:
            print(f"\nUnknown test: {alias}")
            continue

        folder, fn = ALL_TESTS[alias]
        if current_folder != folder:
            current_folder = folder
            print(f"\n[{folder}]")
        print(f"\n{alias}")
        print("-" * len(alias))
        passed, cases = fn()
        total_passed += passed
        total_cases += cases

    print("\n" + "=" * 60)
    print(f"Summary: {total_passed}/{total_cases} passed")
    if total_cases and total_passed == total_cases:
        print("All tests passed!")
    elif total_cases:
        print("Some tests failed.")


if __name__ == "__main__":
    main()

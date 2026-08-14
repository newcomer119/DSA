"""
DSA Practice Runner — run daily tests for any topic from the repo root.

Usage:
    python practice.py                  # run ALL topic tests
    python practice.py list             # list topics and problem counts
    python practice.py hashing            # run one topic
    python practice.py dp greedy          # run multiple topics
    python practice.py hashing coin-change  # run topic + single problem alias
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

TOPICS = {
    "hashing": {
        "path": "leetcode/hashing/run_all_tests.py",
        "desc": "Hash maps, prefix sum, subarray sum/XOR",
    },
    "dp": {
        "path": "leetcode/dynammicprogramming/run_all_tests.py",
        "desc": "1-D and 2-D dynamic programming",
    },
    "greedy": {
        "path": "leetcode/greedy/run_all_tests.py",
        "desc": "Greedy, intervals, heap-based greedy",
    },
    "sliding-window": {
        "path": "leetcode/sliding&twopinters/run_all_tests.py",
        "desc": "Two pointers and sliding window",
    },
    "binary-search": {
        "path": "leetcode/binary-search/run_all_tests.py",
        "desc": "Binary search and variants",
    },
    "backtracking": {
        "path": "leetcode/backtracking/run_all_tests.py",
        "desc": "Backtracking, pruning, combinations",
    },
    "graph": {
        "path": "leetcode/graph/run_all_tests.py",
        "desc": "BFS, DFS, topo sort, Dijkstra, matrix",
    },
    "heap": {
        "path": "leetcode/Heap/run_all_tests.py",
        "desc": "Top-K, merge K lists, median heap",
    },
    "bfs": {
        "path": "leetcode/BFS/run_all_tests.py",
        "desc": "Tree BFS — level order, zigzag, min depth",
    },
}

ALIASES = {
    "hash": "hashing",
    "dynamic-programming": "dp",
    "dynammicprogramming": "dp",
    "two-pointer": "sliding-window",
    "two-pointers": "sliding-window",
    "sliding": "sliding-window",
    "bs": "binary-search",
    "bt": "backtracking",
    "trees": "bfs",
}


def resolve_topic(name: str) -> str | None:
    key = name.lower().replace("_", "-")
    if key in TOPICS:
        return key
    return ALIASES.get(key)


def list_topics() -> None:
    print("=" * 60)
    print("DSA Practice Topics")
    print("=" * 60)
    print(f"\nIndex: {ROOT / 'PRACTICE.md'}\n")
    for key, info in TOPICS.items():
        runner = ROOT / info["path"]
        status = "ready" if runner.exists() else "missing runner"
        print(f"  {key:<18} [{status}]")
        print(f"    {info['desc']}")
        print(f"    python practice.py {key}")
        print()


def run_topic(topic: str, extra_args: list[str] | None = None) -> int:
    info = TOPICS[topic]
    runner = ROOT / info["path"]
    if not runner.exists():
        print(f"Runner not found: {runner}")
        return 1
    cmd = [sys.executable, str(runner)] + (extra_args or [])
    print(f"\n{'=' * 60}")
    print(f"Running: {topic}")
    print(f"{'=' * 60}")
    return subprocess.call(cmd)


def main() -> int:
    args = sys.argv[1:]
    if not args:
        exit_code = 0
        for topic in TOPICS:
            code = run_topic(topic)
            if code != 0:
                exit_code = code
        return exit_code

    if args[0] in ("list", "help", "-h", "--help"):
        list_topics()
        return 0

    # First arg may be topic, rest are passed to topic runner
    topic = resolve_topic(args[0])
    if topic:
        return run_topic(topic, args[1:])

    print(f"Unknown topic: {args[0]}")
    print("Run: python practice.py list")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

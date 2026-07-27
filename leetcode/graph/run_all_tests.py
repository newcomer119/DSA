"""
Daily graph practice checker.

Run all tests:
    python run_all_tests.py

Run one subfolder:
    python run_all_tests.py lc-questions
    python run_all_tests.py matrix

Run one problem:
    python run_all_tests.py islands
    python run_all_tests.py dijkstra
"""

from __future__ import annotations

import importlib.util
import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
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


def norm_lists(groups):
    return sorted(sorted(g) for g in groups)


def norm_strings(items):
    return sorted(items)


def is_valid_course_order(order, n, prereqs):
    if not order:
        return n == 0 or bool(prereqs)
    if len(order) != n or len(set(order)) != n:
        return False
    pos = {c: i for i, c in enumerate(order)}
    for course, prereq in prereqs:
        if pos[prereq] >= pos[course]:
            return False
    return True


def is_valid_task_order(order, tasks, requirements):
    if len(order) != len(tasks):
        return False
    pos = {t: i for i, t in enumerate(order)}
    for a, b in requirements:
        if pos[a] >= pos[b]:
            return False
    return True


# ---------------------------------------------------------------------------
# lc-questions
# ---------------------------------------------------------------------------

def test_course_schedule_ii() -> tuple[int, int]:
    mod = load_module("lc-questions/que1.py")
    sol = mod.Solution()
    tests = [
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], None),
        (1, [], [0]),
        (2, [[0, 1], [1, 0]], []),
    ]
    passed = 0
    for n, prereqs, expected in tests:
        got = sol.findOrder(n, prereqs)
        if expected is None:
            ok = is_valid_course_order(got, n, prereqs)
            name = f"n={n} valid topo"
        else:
            ok = got == expected
            name = f"n={n}"
        if run_case(name, ok, True):
            passed += 1
    return passed, len(tests)


def test_max_network_rank() -> tuple[int, int]:
    mod = load_module("lc-questions/que2.py")
    sol = mod.Solution()
    tests = [(4, [[0, 1], [0, 3], [1, 2], [1, 3]], 4), (2, [[0, 1]], 1), (3, [], 0)]
    passed = 0
    for n, roads, expected in tests:
        if run_case(f"n={n}", sol.maximalNetworkRank(n, roads), expected):
            passed += 1
    return passed, len(tests)


def test_oranges_rotting() -> tuple[int, int]:
    mod = load_module("lc-questions/que3.py")
    sol = mod.Solution()
    tests = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
    ]
    passed = 0
    for grid, expected in tests:
        g = copy.deepcopy(grid)
        if run_case(str(grid), sol.orangesRotting(g), expected):
            passed += 1
    return passed, len(tests)


def test_minesweeper() -> tuple[int, int]:
    mod = load_module("lc-questions/que4.py")
    sol = mod.Solution()
    board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
    expected = [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
    board2 = [row[:] for row in expected]
    expected2 = [row[:] for row in board2]
    expected2[1][2] = "X"
    passed = 0
    if run_case("empty click", sol.updateBoard([r[:] for r in board], [3, 0]), expected):
        passed += 1
    if run_case("mine click", sol.updateBoard([r[:] for r in board2], [1, 2]), expected2):
        passed += 1
    return passed, 2


def test_shortest_path_binary_matrix() -> tuple[int, int]:
    mod = load_module("lc-questions/que5.py")
    sol = mod.Solution()
    tests = [
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ]
    passed = 0
    for grid, expected in tests:
        g = copy.deepcopy(grid)
        if run_case(f"{len(grid)}x{len(grid)}", sol.shortestPathBinaryMatrix(g), expected):
            passed += 1
    return passed, len(tests)


def test_pacific_atlantic_lc() -> tuple[int, int]:
    mod = load_module("lc-questions/que6.py")
    sol = mod.Solution()
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    tests = [(heights, expected), ([[1]], [[0, 0]])]
    passed = 0
    for h, exp in tests:
        if run_case(f"{len(h)}x{len(h[0])}", sol.pacificAtlantic(h), exp):
            passed += 1
    return passed, len(tests)


def test_calc_equation() -> tuple[int, int]:
    mod = load_module("lc-questions/que7.py")
    sol = mod.Solution()
    eqs = [["a", "b"], ["b", "c"]]
    vals = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected = [6.0, 0.5, -1.0, 1.0, -1.0]
    passed = 0
    if run_case("example 1", sol.calcEquation(eqs, vals, queries), expected):
        passed += 1
    eqs2 = [["a", "b"]]
    got2 = sol.calcEquation(eqs2, [0.5], [["a", "b"], ["b", "a"]])
    if run_case("example 3 partial", got2, [0.5, 2.0]):
        passed += 1
    return passed, 2


def test_is_bipartite() -> tuple[int, int]:
    mod = load_module("lc-questions/que8.py")
    sol = mod.Solution()
    tests = [([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False), ([[1, 3], [0, 2], [1, 3], [0, 2]], True), ([[]], True)]
    passed = 0
    for graph, expected in tests:
        if run_case(str(len(graph)), sol.isBipartite(graph), expected):
            passed += 1
    return passed, len(tests)


def test_find_all_recipes() -> tuple[int, int]:
    mod = load_module("lc-questions/que9.py")
    sol = mod.Solution()
    tests = [
        (["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"], ["bread"]),
        (["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"], ["bread", "sandwich"]),
    ]
    passed = 0
    for recipes, ingredients, supplies, expected in tests:
        got = sorted(sol.findAllRecipes(recipes, ingredients, supplies))
        if run_case(str(recipes), got, sorted(expected)):
            passed += 1
    return passed, len(tests)


def test_network_delay() -> tuple[int, int]:
    mod = load_module("lc-questions/que10.py")
    sol = mod.Solution()
    tests = [([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2), ([[1, 2, 1]], 2, 1, 1), ([[1, 2, 1]], 2, 2, -1)]
    passed = 0
    for times, n, k, expected in tests:
        if run_case(f"k={k}", sol.networkDelayTime(times, n, k), expected):
            passed += 1
    return passed, len(tests)


# ---------------------------------------------------------------------------
# weighted, topological-sort, implicit, matrix, vanilla
# ---------------------------------------------------------------------------

def test_dijkstra() -> tuple[int, int]:
    mod = load_module("weighted/dijkstra.py")
    # 0->(1,1), 0->(2,4); 1->(2,2); 2->(3,1)
    graph = [[(1, 1), (2, 4)], [(2, 2)], [(3, 1)], []]
    tests = [(0, 3, 4), (0, 1, 1), (1, 3, 3)]
    passed = 0
    for a, b, expected in tests:
        if run_case(f"{a}->{b}", mod.shortest_path(graph, a, b), expected):
            passed += 1
    return passed, len(tests)


def test_spfa() -> tuple[int, int]:
    mod = load_module("weighted/spfa.py")
    graph = [[(1, 1), (2, 4)], [(2, 2)], [(3, 1)], []]
    if run_case("0->3", mod.shortest_path(graph, 0, 3), 4):
        return 1, 1
    return 0, 1


def test_course_schedule() -> tuple[int, int]:
    mod = load_module("topological-sort/course-schedule.py")
    tests = [(2, [[0, 1]], True), (2, [[0, 1], [1, 0]], False), (3, [[1, 0], [2, 0]], True)]
    passed = 0
    for n, prereqs, expected in tests:
        if run_case(f"n={n}", mod.is_valid_course_schedule(n, prereqs), expected):
            passed += 1
    return passed, len(tests)


def test_alien_dictionary() -> tuple[int, int]:
    mod = load_module("topological-sort/alien-dictionary.py")
    tests = [(["wrt", "wrf", "er", "ett", "rftt"], "wertf"), (["z", "x"], "zx"), (["abc", "ab"], "")]
    passed = 0
    for words, expected in tests:
        if run_case(str(words), mod.alien_order(words), expected):
            passed += 1
    return passed, len(tests)


def test_task_scheduling() -> tuple[int, int]:
    mod = load_module("topological-sort/Task-Scheduling.py")
    tasks = ["a", "b", "c", "d"]
    reqs = [["a", "b"], ["c", "b"], ["b", "d"]]
    got = mod.task_scheduling(tasks, reqs)
    if run_case("example", is_valid_task_order(got, tasks, reqs), True):
        return 1, 1
    return 0, 1


def test_task_scheduling_2() -> tuple[int, int]:
    mod = load_module("topological-sort/task-scheduling2.py")
    got = mod.task_scheduling_2(["a", "b", "c", "d"], [1, 1, 2, 1], [["a", "b"], ["c", "b"], ["b", "d"]])
    if run_case("example", got, 4):
        return 1, 1
    return 0, 1


def test_sequence_reconstruction() -> tuple[int, int]:
    mod = load_module("topological-sort/reconstructing-sequence.py")
    tests = [([1, 2, 3], [[1, 2], [1, 3]], False), ([1, 2, 3], [[1, 2], [1, 3], [2, 3]], True), ([1, 2, 3], [[1, 2]], False)]
    passed = 0
    for original, seqs, expected in tests:
        if run_case(str(original), mod.sequence_reconstruction(original, seqs), expected):
            passed += 1
    return passed, len(tests)


def test_sliding_puzzle() -> tuple[int, int]:
    mod = load_module("implicit/sliding-puzlle.py")
    tests = [([[4, 1, 3], [2, 0, 5]], 5), ([[1, 2, 3], [4, 5, 0]], 0), ([[1, 2, 3], [5, 4, 0]], -1)]
    passed = 0
    for board, expected in tests:
        if run_case(str(board), mod.num_steps(board), expected):
            passed += 1
    return passed, len(tests)


def test_open_the_lock() -> tuple[int, int]:
    mod = load_module("implicit/open-the-lock.py")
    got = mod.num_steps("0202", ["0201", "0101", "0102", "1212", "2002"])
    if run_case("example", got, 6):
        return 1, 1
    return 0, 1


def test_word_ladder() -> tuple[int, int]:
    mod = load_module("implicit/word-ladder.py")
    tests = [
        ("cold", "warm", ["cold", "gold", "cord", "sold", "card", "ward", "warm", "tard"], 4),
        ("hit", "cog", ["hit", "hot", "dot", "dog", "lot", "log", "cog"], 4),
        ("a", "a", ["a"], 0),
    ]
    passed = 0
    for begin, end, words, expected in tests:
        if run_case(f"{begin}->{end}", mod.word_ladder(begin, end, words), expected):
            passed += 1
    return passed, len(tests)


def test_pacific_atlantic() -> tuple[int, int]:
    mod = load_module("matrix/pacific-atlantic.py")
    heights = [[2, 1], [1, 2]]
    expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
    if run_case("2x2", mod.pacific_atlantic_water_flow(heights), expected):
        return 1, 1
    return 0, 1


def test_walls_and_gates() -> tuple[int, int]:
    mod = load_module("matrix/walls-and-gate.py")
    INF = 2147483647
    dungeon = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
    expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
    got = mod.map_gate_distances([row[:] for row in dungeon])
    if run_case("example", got, expected):
        return 1, 1
    return 0, 1


def test_knight_moves() -> tuple[int, int]:
    mod = load_module("matrix/knight-minimum-moves.py")
    tests = [(2, 1, 1), (5, 5, 4), (0, 0, 0)]
    passed = 0
    for x, y, expected in tests:
        if run_case(f"({x},{y})", mod.get_knight_shortest_path(x, y), expected):
            passed += 1
    return passed, len(tests)


def test_num_islands() -> tuple[int, int]:
    mod = load_module("matrix/no-of-islands.py")
    tests = [([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]], 3), ([[1, 0], [0, 1]], 2), ([[0]], 0)]
    passed = 0
    for grid, expected in tests:
        g = copy.deepcopy(grid)
        if run_case(f"grid", mod.count_number_of_islands(g), expected):
            passed += 1
    return passed, len(tests)


def test_flood_fill() -> tuple[int, int]:
    mod = load_module("matrix/flood-fill.py")
    image = [[0, 1, 3, 4, 1], [3, 8, 8, 3, 3], [6, 7, 8, 8, 3], [12, 2, 8, 9, 1], [12, 3, 1, 3, 2]]
    expected = [[0, 1, 3, 4, 1], [3, 9, 9, 3, 3], [6, 7, 9, 9, 3], [12, 2, 9, 9, 1], [12, 3, 1, 3, 2]]
    got = mod.flood_fill(2, 2, 9, [row[:] for row in image])
    if run_case("example", got, expected):
        return 1, 1
    return 0, 1


def test_clone_graph() -> tuple[int, int]:
    mod = load_module("vanilla/clone-graph.py")
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    if run_case("4 nodes", mod.clone_graph(adj), adj):
        return 1, 1
    return 0, 1


def test_vanilla_shortest_path() -> tuple[int, int]:
    mod = load_module("vanilla/shortest-path.py")
    graph = [[1, 2], [0, 2, 3], [0, 1], [1]]
    if run_case("0->3", mod.shortest_path(graph, 0, 3), 2):
        return 1, 1
    return 0, 1


ALL_TESTS = {
    "course-schedule-ii": ("lc-questions", test_course_schedule_ii),
    "max-network-rank": ("lc-questions", test_max_network_rank),
    "oranges-rotting": ("lc-questions", test_oranges_rotting),
    "minesweeper": ("lc-questions", test_minesweeper),
    "binary-matrix-path": ("lc-questions", test_shortest_path_binary_matrix),
    "pacific-atlantic-lc": ("lc-questions", test_pacific_atlantic_lc),
    "calc-equation": ("lc-questions", test_calc_equation),
    "is-bipartite": ("lc-questions", test_is_bipartite),
    "find-all-recipes": ("lc-questions", test_find_all_recipes),
    "network-delay": ("lc-questions", test_network_delay),
    "dijkstra": ("weighted", test_dijkstra),
    "spfa": ("weighted", test_spfa),
    "course-schedule": ("topological-sort", test_course_schedule),
    "alien-dictionary": ("topological-sort", test_alien_dictionary),
    "task-scheduling": ("topological-sort", test_task_scheduling),
    "task-scheduling-2": ("topological-sort", test_task_scheduling_2),
    "sequence-reconstruction": ("topological-sort", test_sequence_reconstruction),
    "sliding-puzzle": ("implicit", test_sliding_puzzle),
    "open-the-lock": ("implicit", test_open_the_lock),
    "word-ladder": ("implicit", test_word_ladder),
    "pacific-atlantic": ("matrix", test_pacific_atlantic),
    "walls-and-gates": ("matrix", test_walls_and_gates),
    "knight-moves": ("matrix", test_knight_moves),
    "num-islands": ("matrix", test_num_islands),
    "flood-fill": ("matrix", test_flood_fill),
    "clone-graph": ("vanilla", test_clone_graph),
    "vanilla-shortest-path": ("vanilla", test_vanilla_shortest_path),
}


def main() -> int:
    filters = [a.lower() for a in sys.argv[1:]]

    if filters:
        selected = {k: v for k, v in ALL_TESTS.items() if any(f in k or f in v[0] for f in filters)}
        if not selected:
            print("Available:", ", ".join(ALL_TESTS))
            return 1
    else:
        selected = ALL_TESTS

    total_passed = 0
    total_cases = 0
    failed = []
    current_folder = None

    print("=" * 60)
    print("Graph Daily Tests")
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

"""
Guard against module-level LeetCode solutions using `self`.

When a function is defined at module scope with `self` but attached to a
Solution instance for local tests (e.g. `sol.method = fn`), Python does not
bind `self` and calls like `sol.method(nums, target)` fail.

Run from repo root:
    python check_solution_binding.py
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def module_level_self_functions(path: Path) -> list[tuple[int, str]]:
    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError:
        return []

    issues: list[tuple[int, str]] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.args.args:
            first = node.args.args[0].arg
            if first == "self":
                issues.append((node.lineno, node.name))
    return issues


def main() -> int:
    py_files = sorted(ROOT.rglob("*.py"))
    py_files = [p for p in py_files if "check_solution_binding.py" not in p.name]

    violations: list[tuple[Path, int, str]] = []
    for path in py_files:
        if not path.is_file():
            continue
        try:
            rel_path = path.relative_to(ROOT)
            issues = module_level_self_functions(path)
        except (OSError, UnicodeDecodeError):
            continue
        for lineno, name in issues:
            violations.append((rel_path, lineno, name))

    if not violations:
        print(f"OK: checked {len(py_files)} Python files — no module-level `self` functions.")
        return 0

    print("Module-level functions must not take `self`.")
    print("Define methods inside `class Solution:` or drop `self` for standalone functions.\n")
    for rel_path, lineno, name in violations:
        print(f"  {rel_path}:{lineno}  def {name}(self, ...)")
    print(f"\n{len(violations)} issue(s) in {len({v[0] for v in violations})} file(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

# Given a linked list with potentially a loop, determine whether the linked list from the first node contains a cycle in it. For bonus points, do this with constant space.

# Parameters
# nodes: The first node of a linked list with potentially a loop.
# Result
# Whether there is a loop contained in the linked list.
# Examples
# Example 1
# Input:
# Output:
# true
# Example 2
# Input:
# Output:
# false
# Constraints
# 1 <= len(nodes) <= 10^5

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return False 

    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow == fast:
            return True 

    return False 
    

# --- Daily tests ---
if __name__ == "__main__":
    def build_list(values):
        if not values:
            return None
        head = Node(values[0])
        cur = head
        for v in values[1:]:
            cur.next = Node(v)
            cur = cur.next
        return head

    def build_cycle(values, pos):
        nodes = [Node(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos >= 0:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    TESTS = [
        ("no cycle", build_list([1, 2, 3]), False),
        ("cycle", build_cycle([1, 2, 3, 4], 1), True),
        ("single", Node(1), False),
    ]
    passed = 0
    for name, head, exp in TESTS:
        got = has_cycle(head)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {name} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
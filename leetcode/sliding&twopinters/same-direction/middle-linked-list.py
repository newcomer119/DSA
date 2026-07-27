# Middle of a Linked List
# Find the middle node of a linked list.

# Input: 0 1 2 3 4

# Output: 2

# If the number of nodes is even, then return the second middle node.

# Input: 0 1 2 3 4 5

# Output: 3



class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    return slow.val

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([0, 1, 2, 3, 4], 2), ([0, 1, 2, 3, 4, 5], 3), ([1], 1)]
    passed = 0
    for values, exp in TESTS:
        head = build_list(iter(values), int)
        got = middle_of_linked_list(head)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {values} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
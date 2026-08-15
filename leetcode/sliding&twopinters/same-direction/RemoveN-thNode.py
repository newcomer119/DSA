# Problem
# Given the head of a linked list and an integer n, remove the n-th node from the end of the list and return the head of the modified list.

# Input:

# head: the head node of a singly linked list
# n: an integer representing the position from the end (1-indexed)
# Output:

# Return the head of the modified linked list
# Constraints:

# The list has at least 1 node
# n is a valid position from the end (1 <= n <= length of list)
# Examples:

# Example 1:

# Input: head = [1, 2, 3, 4], n = 1
# Output: [1, 2, 3]
# Explanation: Remove the 1st node from the end (value 4)
# Example 2:

# Input: head = [1, 2, 3, 4], n = 2
# Output: [1, 2, 4]
# Explanation: Remove the 2nd node from the end (value 3)
# Example 3:

# Input: head = [1, 2, 3, 4], n = 4
# Output: [2, 3, 4]
# Explanation: Remove the 4th node from the end (the head, value 1)

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    if head is None or n < 1:
        return head 

    dummy = Node(0)
    dummy.next = head
    fast = dummy
    for _ in range(n):
        if fast.next is None:
            return head 

        fast = fast.next 

    slow = dummy 
    while fast and fast.next:
        fast = fast.next 
        slow = slow.next 
    slow.next = slow.next.next 
    return dummy.next
    # if head is None or n < 1:
    #     return head 
    # dummy = Node(0)
    # dummy.next = head
    # fast = dummy
    # for _ in range(n):
    #     if fast.next is None:
    #         return head 
    #     fast = fast.next
    # slow = dummy
    # while fast and fast.next:
    #     fast = fast.next
    #     slow = slow.next 
    # slow.next = slow.next.next
    # return dummy.next 

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

    def to_list(head):
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out

    TESTS = [([1, 2, 3, 4], 1, [1, 2, 3]), ([1, 2, 3, 4], 2, [1, 2, 4]), ([1], 1, [])]
    passed = 0
    for values, n, exp in TESTS:
        got = to_list(remove_nth_from_end(build_list(values), n))
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

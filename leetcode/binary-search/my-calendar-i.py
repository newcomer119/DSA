# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

# Constraints:

# 0 <= start < end <= 109
# At most 1000 calls will be made to book.



class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        left= 0
        right = len(self.calendar) - 1
        idx = len(self.calendar)
        while left <= right : 
            mid = (left + right) // 2
            if self.calendar[mid][0] > start:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        if (idx > 0 and self.calendar[idx-1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.insert(idx, (start, end))
        return True


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([(10, 20), (15, 25), (20, 30)], [True, False, True]),
        ([(1, 5), (5, 10), (10, 15)], [True, True, True]),
        ([(2, 8), (3, 9)], [True, False]),
    ]
    passed = 0
    for bookings, expected in TESTS:
        cal = MyCalendar()
        got = [cal.book(s, e) for s, e in bookings]
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] bookings={bookings} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")
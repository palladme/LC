from typing import deque

class RecentCounter:

    def __init__(self):
        self.dequeue = deque()

    def ping(self, t: int) -> int:
        self.dequeue.append(t)

        while t - self.dequeue[0] > 3000:
            self.dequeue.popleft()

        return len(self.dequeue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

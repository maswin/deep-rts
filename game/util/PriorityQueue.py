import heapq


class PriorityQueue:
    def __init__(self, e):
        self.elements = e
        self.l = 0

    def empty(self):
        return len(self.elements) == 0

    def toJSON(self):
        return self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
        self.l += 1

    def get(self):
        if self.l > 0:
            self.l -= 1
            return heapq.heappop(self.elements)[1]

        return None

    def __iter__(self):
        return iter([x[1] for x in self.elements])
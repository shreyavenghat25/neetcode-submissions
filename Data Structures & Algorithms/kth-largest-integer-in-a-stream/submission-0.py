import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # save k and create empty min heap
        self.k = k
        self.heap = []

        # add all initial numbers
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # push new value into heap
        heapq.heappush(self.heap, val)

        # if heap is bigger than k, remove smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # top of heap = kth largest
        return self.heap[0]
        

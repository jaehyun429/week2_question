class PriorityQueue:
  def __init__(self):
    self.heap = []
    self.counter = 0  # tie-breaker for FIFO when priorities are equal

  def push(self, item, priority):
    entry = (priority, self.counter, item)
    self.heap.append(entry)
    self._sift_up(len(self.heap) - 1)
    self.counter += 1

  def pop(self):
    if len(self.heap) > 1:
      self._swap(0, len(self.heap) - 1)
      _, _, item = self.heap.pop()
      self._sift_down(0)
      return item
    elif len(self.heap) == 1:
      _, _, item = self.heap.pop()
      return item
    else:
      return None

  def _sift_up(self, index):
    while index > 0:
      parent_index = (index - 1) // 2
      if self.heap[parent_index] > self.heap[index]:
        self._swap(parent_index, index)
        index = parent_index
      else:
        break

  def _sift_down(self, index):
    length = len(self.heap)
    while True:
      left = 2 * index + 1
      right = 2 * index + 2
      smallest = index

      if left < length and self.heap[left] < self.heap[smallest]:
        smallest = left
      if right < length and self.heap[right] < self.heap[smallest]:
        smallest = right

      if smallest != index:
        self._swap(index, smallest)
        index = smallest
      else:
        break

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

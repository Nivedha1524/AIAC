class QueueFullException(Exception):
    """Raised when trying to enqueue to a full Queue."""
    pass

class QueueEmptyException(Exception):
    """Raised when trying to dequeue from an empty Queue."""
    pass

class Queue:
    """
    A simple Queue implementation with optional maximum size.

    Methods:
        enqueue(item): Add item to the back of the queue. Raises QueueFullException if full.
        dequeue(): Remove and return the item from the front. Raises QueueEmptyException if empty.
        front(): Return the front item without removing. Raises QueueEmptyException if empty.
        is_empty(): Returns True if the queue is empty.
        is_full(): Returns True if the queue has reached its max size (bounded queues).
        size(): Returns the number of items in the queue.
    """
    def __init__(self, max_size=None):
        """
        Initialize the queue.
        Args:
            max_size (int or None): Maximum size for bounded queue, or None for unlimited size.
        """
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        """
        Add an item to the back of the queue.
        Raises QueueFullException if the queue is bounded and full.
        """
        if self.max_size is not None and len(self.items) >= self.max_size:
            raise QueueFullException("Queue is full (max_size={})".format(self.max_size))
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        Raises QueueEmptyException if the queue is empty.
        """
        if not self.items:
            raise QueueEmptyException("Queue is empty")
        return self.items.pop(0)

    def front(self):
        """
        Return the item at the front of the queue without removing it.
        Raises QueueEmptyException if the queue is empty.
        """
        if not self.items:
            raise QueueEmptyException("Queue is empty")
        return self.items[0]

    def is_empty(self):
        """Returns True if the queue is empty, else False."""
        return len(self.items) == 0

    def is_full(self):
        """
        Returns True if the queue has reached its maximum size (only for bounded queues).
        """
        return self.max_size is not None and len(self.items) >= self.max_size

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.items)

# ---- TEST CASES ----

def test_unbounded_queue():
    print("Testing unbounded (unlimited size) queue...")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.front() == 10
    assert q.dequeue() == 10
    assert q.front() == 20
    assert not q.is_empty()
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.is_empty()
    try:
        q.dequeue()
    except QueueEmptyException:
        print("Pass: Caught QueueEmptyException on empty dequeue")
    else:
        print("Fail: Did not catch QueueEmptyException")

def test_bounded_queue():
    print("Testing bounded (max size) queue...")
    q = Queue(max_size=2)
    assert not q.is_full()
    q.enqueue("A")
    assert not q.is_full()
    q.enqueue("B")
    assert q.is_full()
    try:
        q.enqueue("C")
    except QueueFullException:
        print("Pass: Caught QueueFullException on enqueue to full queue")
    else:
        print("Fail: Did not catch QueueFullException")

    assert q.front() == "A"
    assert q.dequeue() == "A"
    assert not q.is_full()
    q.enqueue("C")
    assert q.is_full()
    assert q.dequeue() == "B"
    assert q.dequeue() == "C"
    assert q.is_empty()
    try:
        q.front()
    except QueueEmptyException:
        print("Pass: Caught QueueEmptyException on front from empty queue")
    else:
        print("Fail: Did not catch QueueEmptyException")

if __name__ == "__main__":
    test_unbounded_queue()
    test_bounded_queue()
    print("All tests completed.")
"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adding and removing at the same end makes the newest item leave first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Raise a clear error when there is nothing to remove.
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        # Read the last value while leaving it in the stack.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New items join the back so the oldest item can leave from the front.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Raise a clear error when there is nothing to remove.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")
        # Read the oldest value while leaving it in the queue.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ==============================
    # TODO (Student): STACK DEMO
    # ==============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    stack = Stack()

    for value in [10, 20, 30, 40]:
        stack.push(value)
        print(f"Added {value} to the top of the stack.")

    print(f"Peek returns {stack.peek()} without removing it.")

    print("\nLIFO: The last value added is removed first.")
    print("Expected removal order: 40, 30, 20, 10")

    while not stack.is_empty():
        print(f"Removed from stack: {stack.pop()}")

    print(f"Stack is empty: {stack.is_empty()}")

    # Catch the errors so the remaining examples can still run.
    print("\nUsing pop() on an empty stack:")
    try:
        stack.pop()
    except IndexError as error:
        print(error)

    print("\nUsing peek() on an empty stack:")
    try:
        stack.peek()
    except IndexError as error:
        print(error)

    print("\nTesting a stack with one item:")
    single_stack = Stack()
    single_stack.push(99)
    print("Added 99 to the stack.")
    print(f"Empty before removal: {single_stack.is_empty()}")
    print(f"Removed: {single_stack.pop()}")
    print(f"Empty after removal: {single_stack.is_empty()}")

    # ==============================
    # TODO (Student): QUEUE DEMO
    # ==============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    for value in [10, 20, 30, 40]:
        queue.enqueue(value)
        print(f"Added {value} to the back of the queue.")

    print(f"Front returns {queue.front()} without removing it.")

    print("\nFIFO: The first value added is removed first.")
    print("Expected removal order: 10, 20, 30, 40")

    while not queue.is_empty():
        print(f"Removed from queue: {queue.dequeue()}")

    print(f"Queue is empty: {queue.is_empty()}")

    # Catch the errors so the remaining examples can still run.
    print("\nUsing dequeue() on an empty queue:")
    try:
        queue.dequeue()
    except IndexError as error:
        print(error)

    print("\nUsing front() on an empty queue:")
    try:
        queue.front()
    except IndexError as error:
        print(error)

    print("\nTesting a queue with one item:")
    single_queue = Queue()
    single_queue.enqueue(99)
    print("Added 99 to the queue.")
    print(f"Empty before removal: {single_queue.is_empty()}")
    print(f"Removed: {single_queue.dequeue()}")
    print(f"Empty after removal: {single_queue.is_empty()}")

    # Real-world scenario: a support desk.
    # Tickets are handled in arrival order using a queue.
    # Recent actions are removed in reverse order using a stack.
    print("\n=== SUPPORT DESK SCENARIO ===")

    tickets = Queue()
    history = Stack()

    tickets.enqueue("Reset password")
    tickets.enqueue("Fix printer")
    tickets.enqueue("Install software")

    print(f"Next ticket: {tickets.front()}")

    while not tickets.is_empty():
        ticket = tickets.dequeue()
        print(f"Handled ticket: {ticket}")
        history.push(f"Handled: {ticket}")

    print("\nRemoving the latest action from history:")
    print(history.pop())
    # Removing a history entry does not restore the ticket.


if __name__ == "__main__":
    main()

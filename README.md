# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

For this assignment, i used a Python list for stack and deque from Python's collections module for the queue. I tested both with 10, 20, 30, and 40. The stack removed 40 first because items were added and removed from the same end. This showed LIFO, or last in, first out. The queue removed 10 first because items were added at the back and removed from the front. This showed FIFO, or first in, first out.

One problem I had was getting IntelliJ to find the Python interpreter. After selecting it in the run configuration, the program ran. I also tested empty structures and single-item cases. Catching the errors let the rest of the examples keep running.

For my real-world example, I used a support desk. The queue handled tickets in arrival order, while the stack kept the action history. Removing the latest history entry did not return the ticket to the queue.
Both structures used O(n) space, so more stored items meant more memory was needed. Seeing the removal order helped me understand when to use each structure.

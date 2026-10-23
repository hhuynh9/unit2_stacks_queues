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

I used a Python list for the stack and collections.deque for the
queue. I left the TODO comments in place and added comments to explain what the code did.

I added 10, 20, 30, and 40 to both. The stack took out 40 first, and the queue took out 10 first. 
I also checked what happened when
they were empty. The program printed an error message and kept
going. Then I tried each one with just one item. After removing that item, is_empty() returned True.

For the real-world example, I added a support desk. Tickets went
into a queue and were handled in the order they came in. The stack
kept a history of those actions. When I removed an entry from the
history, it took out the most recent one. It did not put the ticket back in the queue.

Both structures used O(n) space. Basically, the more items they held, the more memory they needed.
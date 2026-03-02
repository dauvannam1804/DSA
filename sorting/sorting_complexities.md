# Sorting Algorithms Complexities and Use Cases

This document provides an overview of the time and space complexity for various sorting algorithms, along with common scenarios where each algorithm should be used.

## Complexity Table

| Algorithm | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) |

## When to use which algorithm?

*   **Quick Sort**: Generally the fastest sorting algorithm in practice for large generic datasets. It is often the default choice in many standard libraries. Use when average-case performance is crucial and memory is somewhat limited (in-place sort), though it's not stable.
*   **Merge Sort**: The best choice when stability is a requirement (preserving the relative order of equal elements) and guaranteed O(n log n) worst-case time complexity is needed. Excellent for sorting linked lists or very large datasets that do not fit into memory (external sorting).
*   **Heap Sort**: Extremely useful when memory is strictly limited and a consistent O(n log n) time complexity is needed. Unlike Merge Sort, it doesn't require O(n) extra space, and unlike Quick Sort, its worst-case scenario isn't O(n²). However, it's typically slower in practice than a well-implemented Quick Sort due to poor cache locality.
*   **Bubble Sort**: Mostly an educational algorithm. It is rarely used in real-world applications because of its terrible O(n²) average and worst-case time complexity. Use only if the dataset is extremely small and almost perfectly sorted.
*   **Insertion Sort**: Very efficient for extremely small datasets or datasets that are already substantially sorted (where it approaches O(n) time). It is heavily used in hybrid algorithms like Tim Sort and Introsort to deal with small subproblems once the data is partitioned.
*   **Selection Sort**: Its main advantage is that it makes the absolute minimum number of memory writes (O(n) swaps). Use this algorithm primarily in situations where writing to memory is heavily constrained or significantly more expensive than reading from it (e.g., writing to certain types of flash memory).

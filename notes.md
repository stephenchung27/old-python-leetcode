# Programming Techniques

## K smallest / largest elements

### Heap Method - `O(nlogn)`
1. Create a `K` sized heap.
2. If we're looking for the smallest / largest, make the heap track the inverse.
3. Disregard any elements larger / smaller than the top of the Min Heap.
4. The remaining elements in the heap are the smallest / largest elements.

### Quick Select - Average: `O(n)`, Worst: `O(n^2)`
1. Select a random element from the array. (Sometimes a heuristic can be applied to choose a better element.)
2. Swap elements to the left or right of the given element given their relation to that element.
3. Determine what index that chosen element is placed at the end of the swap.
    - If the index is K, then you have found the K smallest / largest elements.
    - If the index is larger than K, Quick Select the subarray up to the index.
    - If the index is smaller than K, Quick select the subarray from the index.

## Intervals

### Identifying Conflicting Intervals
Given two intervals with a start and an end the following conditional identifies any conflicts.
```Python
first.start < second.end and first.end > second.start
```


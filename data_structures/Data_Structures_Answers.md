Add your answers to the questions below.

1.  What is the runtime complexity of your `depth_first_for_each` method? O(n)

2.  What is the space complexity of your `depth_first_for_each` function? O(1)

3.  What is the runtime complexity of your `breadth_first_for_each` method? O(n)

4.  What is the space complexity of your `breadth_first_for_each` method? O(n)

5.  What is the runtime complexity of your `heapsort` function?
    5.1 FIRST Creating the Heap O( summatory\*1->n(nlogn) ) , may I said: O(nlogn)? \*\*\* I'll appreciate any comments on this \_\*\*
    5.2 SORTING Heap.delete() - O(nlogn)
    5.3 SORTING O(n)
    5.4 THUS : O( nlogn + nlogn + n ) -> O( 2(nlogn) + n ) -> MAY I SAID: runtime complexity for `heapsort` is O( nlogn )

6.  What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data.
    6.1 Space for the created `heap` -> O(n)
    6.2 Space for the `sorted list` -> O(n)
    6.3 THUS O( 2n ) -> O(n)

- What would be the space complexity if your function instead altered the input array?
  6.1 Space for the created `heap` -> O(n)

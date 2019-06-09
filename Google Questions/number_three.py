'''
Given an array of integers arr[], find the number of recycled pairs in the array. 
A recycled pair of two numbers {a, b} has the following properties :

A should be smaller than B. Number of digits should be same. 
By rotating A any number of times in one direction, we should get B.

From my understanding a recycled pair would be
(123, 231)
Where a=123 and b=231

For each tuple we'd first check if a < 0
  if so iterate through the digits a
Fr

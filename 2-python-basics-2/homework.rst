
======================================
EPAM Python for QA Training
======================================

Homework 2
===========

Level 1
--------

1. Write a function which takes a string and returns the first 10
characters off it concatenated with the last 10 characters.

2. Write a function that takes a comma-separated string and returns a 
last element (separated by a last comma) or the entire string if there is
no comma in it.

3. Write a function that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates::

    [1, 2, 3, 4, 4, 6, 2] -> [1, 3, 6]

Level 2
--------

4. Write program to evaluate ``(a or not b) and (c or not a)`` expression
for boolean varibles `a`, `b`, `c` showing result for all possible
variables combinations.

5. Write a function to return the sum of the numbers in the array,
returning 0 for an empty array. Except the number 13 is very unlucky, so it
does not count and numbers that come immediately after a 13 also do not count.
Array could contain strings and boolean values (do not count them)::

    sum13([1, 2, 2, 1]) -> 6
    sum13([1, 1]) -> 2
    sum13([1, 2, 2, 1, 13]) -> 6
    sum13([1, 2, 2, 1, 13, 5, 4, 2]) -> 6

6. Write a function that returns dictionary where keys are even numbers
between 1 and n and values are keys in square, by default n = 100.

Level3
--------

7. Write a function to find is word palindrome.
Please use next validation procedure: calculate each letter occurrence in
word, word will be palindrome if all letters occurrences count іs even number
except one possible odd number.

    racecar
        r -> 2, a -> 2, c -> 2, e -> 1
    anna
        a -> 2, n -> 2

.. some examples copied from https://github.com/vkhoroz/python-training/

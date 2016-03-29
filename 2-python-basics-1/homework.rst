
======================================
EPAM Python for QA Training
======================================

Homework 2-1
===========

Level 1
--------

1. Write a program to calculate expression::

    1 + 2a    4(b + c)(5 - d - e)     7     2
    ------  + ------------------- - 6(- + h)
      3               f               g

where a = 32, b = 37.2, c = -102.345, d = 45, e = 11, f = 3, g = 0.002, h = 11.

2. Print this ASCII graphic using 4 different string literal types::

    _-_-_-_-_-_-_
    \           /
    |  ^_____^  |
    /  (.) (.)  \
    |  ( t   )  |  Miaowww
    \    ==/    /
    |           |
    '"'"'"'"'"'"'

3. Print unique elements from any given list or tuple.

Level 2
--------

4. Write a program to calculate the number of times that the string 'hi'
   appears anywhere in the given string and change 'hi' to 'bye'. Case should
   be ignored.

5. Unite three lists to one and print it in reverse order::

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]

Level 3
--------

6. Having tuple ``('postgresql', 
   'semantic.amazonaws-prod.com', 5432, 'semantic', 'admin', '12345')`` with
   production database connection properties (dialect, host, port, database
   name, user name, password). Program should:

    - create ``prod_config`` dictionary, where dict keys are connection
      properties names and dict values are appropriate values from input tuple;

    - create ``staging_config`` dictionary with the same keys and values as 
      ``prod_config``;

    - in ``staging_config`` change host to
      'semantic.amazonaws-staging.com' and password to 'root';

    - for ``prod_config`` and ``staging_config`` print connection strings in
      format
      ``{dialect}://{user name}:{password}@{host}:{post}/{database name}``

.. some examples copied from https://github.com/vkhoroz/python-training/

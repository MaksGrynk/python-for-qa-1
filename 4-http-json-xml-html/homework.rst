
======================================
EPAM Python for QA Training
======================================

Homework 4
===========

Level 1
--------

1. Write a function to get product price from web page for
   `Deshevshe <http://deshevshe.net.ua/>`_ site.Handle the case when a product
   is out of stock.

2. Please change ownership for all issues in ``bugs.json`` to 'qa5'. Save
   result to ``bugs_new.json``. Use json loads and dumps methods.

3. Write a script to parse ``habraharb_all.xml`` and print each article's
   title, author and list with categories.


Level 2
--------

4. Transform ``course.xml`` to HTML:

    - tag `name` -> <title>;

    - `modules` -> <article> in <body> with <h1> for module name;

    - `examples` -> <ul> and <li>;


5. Having data file with web site clients ``clients.json``, find clients
   who don't have access to `web service
   <https://python-for-qa.herokuapp.com/login>`_ (site uses Basic
   Authentication).


Level 3
--------

6. Write a program to compare web service result in XML and JSON formats.
   Here is the information about web service:

    - url: https://python-for-qa.herokuapp.com/data

    - uses token based authentication, token should be passed in request
      header: ``X-AUTH-TOKEN``

    - to get token send GET request to
      https://python-for-qa.herokuapp.com/login (Basic Authentication,
      user=``admin``, password=``password``)

    - service returns data in XML and JSON formats based on ``Accept`` header

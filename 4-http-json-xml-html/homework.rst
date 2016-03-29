
======================================
EPAM Python for QA Training
======================================

Homework 4
===========

Level 1
--------

1. Write a function to get product price from web page for site
   `Deshevshe <http://deshevshe.net.ua/>`_. Handle case if product is out of
   stock

2. Please change ownership for all issues in ``bugs.json`` to 'qa5'. Save
   result to ``bugs_new.json``. Use json loads and dumps methods.

3. XSLT transformation


Level 2
--------

4. Write a script to parse ``habraharb_all.xml`` and print each article's
   title, author and list with categories


5. Having data file with web site clients ``clients.json``. Find clients
   who don't have access to `web site <http://localhost/>`_ (uses Basic
   Authentication)


Level 3
--------

6. Write a program to compare web service result in XML and JSON formats.
   Information about web service is:

    - url: http://localhost/

    - uses token based authentication, token should be passed in request
      header: ``X-AUTH-TOKEN``

    - to get token send GET request to http://localhost/login (Basic
      Authentication, user=``admin``, password=``password``)

    - service returns data in XML and JSON formats based on ``Accept`` header



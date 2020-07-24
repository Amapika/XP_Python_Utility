Aiohttp Demo
=========

Bank Rest-Operation with Aiohttp
Installation
============

Clone repo and install library::

https://github.com/Amapika/Aiohttp_Framework.git

Run application::

    $ python app.py

Open browser::

    http://127.0.0.1:8080

Try run your application now and send a POST request to http://localhost:8080/user?name=test&acc_no=1231311&balance=12000

    [GET] for checkBalance:-
    http://localhost:8080/user/checkBalance  (localhost:8080/user/checkBalance )
    
    [POST]for withdraw:-
    http://localhost:8080/user/withdraw?amt=12 (localhost:8080/user/withdraw?amt=12 )
    
    [PUT]deposite:-
    http://localhost:8080/user/deposit?amt=23123 (localhost:8080/user/deposit?amt=23123)

Requirements
============
* aiohttp_


.. _Python: https://www.python.org
.. _aiohttp: https://github.com/aio-libs/aiohttp

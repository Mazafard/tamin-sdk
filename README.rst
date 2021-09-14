Python library for Tamin.ir API
=====================================

.. image:: https://badge.fury.io/py/taminsdk.svg
    :target: https://badge.fury.io/py/taminsdk
.. image:: https://app.travis-ci.com/Mazafard/tamin-sdk.svg?branch=master
    :target: https://travis-ci.org/mazafard/tamin-sdk


This is a Python library for the `tamin.ir
API <https://tamin.ir>`__. Using this, you can interact
with tamin.ir from your Python applications. It supports Python
2.7 and Python 3 (3.6+). For more about information about the
tamin.ir API, visit https://tamin.ir.

Install
~~~~~~~

Install it using ``pip install taminsdk``. It may be a good idea to
use `virtualenv <https://virtualenv.readthedocs.org/en/latest/>`__ as
part of your workflow.

Versioning
----------

The current version `series` of the library is ``0.1.x`` which corresponds to the
``0.1`` version of the API. The revision number ``x`` corresponds to the
revision of the SDK. The ``0.1`` series of the library will continue to
support (in a backward compatible way) the ``0.1`` version of the
Tamin.ir API.

Usage
~~~~~

The first step to using any SDK function is to create a `Session` object:

::

    >>> from taminsdk.session import Session
    >>> session = Session(oauth_token=token)

You must have a valid OAuth2 token before you can use the SDK or the
API. See the `Tamin.ir Developer
portal <https://tamin.ir>`__ for more information on
how you can do so.

Once we have a session object, we can start using the SDK functions.

Examples
~~~~~~~~

All the examples below recognizes two environment variables:

-  ``OAUTH_TOKEN``: The OAuth2 token to create the session with and
   must be specified
-  ``URL``: If you want to use the library to make requests against
   the `tamin.ir
   Sandbox <https://Tamin.ir>`__,
   you can specify ``URL=https://ep-test.tamin.ir/api/``. If
   not specified, it defaults to ``http://soa.tamin.ir/interface/epresc``.

**Prescription**

-  `Create a Prescription <examples/create_prescription.py>`__

License
~~~~~~~

GNU LGPLv3. Please see `LICENSE <LICENSE>`__.

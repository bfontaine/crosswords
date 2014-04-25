==========
crosswords
==========

.. image:: https://img.shields.io/travis/bfontaine/crosswords.png
   :target: https://travis-ci.org/bfontaine/crosswords
   :alt: Build status

.. image:: https://img.shields.io/coveralls/bfontaine/crosswords/master.png
   :target: https://coveralls.io/r/bfontaine/crosswords?branch=master
   :alt: Coverage status

.. image:: https://img.shields.io/pypi/v/crosswords.png
   :target: https://pypi.python.org/pypi/crosswords
   :alt: Pypi package

.. image:: https://img.shields.io/pypi/dm/crosswords.png
   :target: https://pypi.python.org/pypi/crosswords

**crosswords** is a terminal tool to help you solving crosswords.

This is a full rewrite of a script I wrote back in 2011 to help my girlfriend
solve crosswords.

Install
-------

.. code-block::

    pip install crosswords

To upgrade a previous installation, use:

.. code-block::

    pip install -U crosswords

Run
---

.. code-block::

    crosswords <word>

Your word should have ``?``s for each letter you don't know, e.g.: `bon??ur`.

Tests
-----

Clone this repo, then: ::

    [sudo] make deps
    make check


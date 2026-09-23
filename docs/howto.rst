.. _how-to:

How to use esprsim
==================

Installation
------------

Install the package from the repository root:

.. code-block:: bash

   pip install -e .

Quick start
-----------

<tbd>

Post-processing
---------------

Post-processing is very model specific, ``esprsim`` has only a few extraction methods
for specific metrics using ``res`` (feel free to extend the available methods and add
them to the project).

The examples use the .csv file created by 'xml output'. The value set according to the
list of desired output parameters found in the example model 'input.xml' is available
for the creation of graphics or statistics.

.. note::
   ESP-r must be compiled to use the xml-output feature for the examples to run
   correctly by setting ``--xml`` in the command line of ``Install``.

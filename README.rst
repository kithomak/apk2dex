apk2dex
=======

.. comment
    .. image:: https://img.shields.io/pypi/v/apk2dex.svg
        :target: https://pypi.python.org/pypi/apk2dex
        :alt: Latest PyPI version

.. comment
    .. image:: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal.png
        :target: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal
        :alt: Latest Travis CI build status

A very raw APK to DEX file extractor.


Installation
------------

Clone the project

.. code:: bash

   git clone https://github.com/kithomak/apk2dex.git

and then run

.. code:: bash

   python setup.py install

from the project root folder.


Usage
-----

From the project root folder, run

.. code:: bash

   python apk2dex <input> [-o output] [options]

For example:

.. code:: bash

   python apk2dex my_apk_file.apk my_output_folder -v

After installation, you can run from any folder (note the ``-m`` flag):

.. code:: bash

    python -m apk2dex <input> [-o output] [options]

Optional arguments:

-o      Output folder. Defaults to the current working folder.
-v      Print progress info and error message to stdout.


Requirements
^^^^^^^^^^^^

Python 3.3 or up will do. You will need ``tqdm`` if you want to display a progress bar for bulk extraction.
You may install ``tqdm`` via ``pip``.


License
-------

MIT


Authors
-------

``apk2dex`` was written by `Kit-Ho Mak <kithomak23@gmail.com>`_.

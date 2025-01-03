Naomi
=====

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/Agent Naomi.svg
   :target: https://pypi.org/project/Agent Naomi/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/Agent Naomi.svg
   :target: https://pypi.org/project/Agent Naomi/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/Agent Naomi
   :target: https://pypi.org/project/Agent Naomi
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/Agent Naomi
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/Agent Naomi/latest.svg?label=Read%20the%20Docs
   :target: https://Agent Naomi.readthedocs.io/
   :alt: Read the documentation at https://Agent Naomi.readthedocs.io/
.. |Tests| image:: https://github.com/mimipynb/Agent Naomi/workflows/Tests/badge.svg
   :target: https://github.com/mimipynb/Agent Naomi/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/mimipynb/Agent Naomi/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/mimipynb/Agent Naomi
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

The project environment for Naomi is controlled by `conda` 
and `poetry`; the former for maintaining the Python environment, as well as additional 
libraries like CUDA, and the latter for Python specific dependencies. There is
a bit of overlap between these two tools, however mostly because `conda`
is not great for resolving dependencies, and `poetry` can't handle things
that aren't Python (e.g. MPI, MKL).

The recommended procedure from scratch is to follow these steps:

.. code:: console

   $ conda create -n agentNaomi python=3.7
   $ conda activate agentNaomi
   $ pip install poetry
   $ poetry install

Usage
-----

Please see the `Command-line Reference <Usage_>`_ for details.


Project Structure
-----------------

The project filestructure is laid out as such::

   ├── CITATION.cff
   ├── codecov.yml
   ├── CODE_OF_CONDUCT.rst
   ├── CONTRIBUTING.rst
   ├── data
   │   ├── external
   │   ├── interim
   │   ├── processed
   │   └── raw
   ├── docs
   │   ├── codeofconduct.rst
   │   ├── conf.py
   │   ├── contributing.rst
   │   ├── index.rst
   │   ├── license.rst
   │   ├── reference.rst
   │   ├── requirements.txt
   │   └── usage.rst
   ├── environment.yml
   ├── models
   ├── notebooks
   │   ├── dev
   │   ├── exploratory
   │   └── reports
   ├── noxfile.py
   ├── poetry.lock
   ├── pyproject.toml
   ├── README.rst
   ├── scripts
   │   └── train.py
   └── src
      └── agentNaomi
         ├── __init__.py
         ├── layers
         │   ├── __init__.py
         │   ├── layers.py
         │   └── tests
         │       ├── __init__.py
         │       └── test_layers.py
         ├── __main__.py
         ├── models
         │   ├── __init__.py
         │   ├── models.py
         │   └── tests
         │       ├── __init__.py
         │       └── test_models.py
         ├── pipeline
         │   ├── data.py
         │   ├── __init__.py
         │   ├── tests
         │   │   ├── __init__.py
         │   │   ├── test_data.py
         │   │   └── test_transforms.py
         │   └── transforms.py
         └── utils.py

A brief summary of what each folder is designed for:

#. `data` contains copies of the data used for this project. It is recommended to form a pipeline whereby the `raw` data is preprocessed, serialized to `interim`, and when ready for analysis, placed into `processed`.
#. `models` contains serialized weights intended for distribution, and/or testing.
#. `notebooks` contains three subfolders: `dev` is for notebook based development, `exploratory` for data exploration, and `reports` for making figures and visualizations for writeup.
#. `scripts` contains files that meant for headless routines, generally those with long compute times such as model training and data cleaning.
#. `src/agentNaomi` contains the common code base for this project.


Code development
----------------

All of the code used for this project should be contained in `src/agentNaomi`,
at least in terms of the high-level functionality (i.e. not scripts), and is intended to be
a standalone Python package.

The package is structured to match the abstractions for deep learning, specifically PyTorch, 
PyTorch Lightning, and Weights and Biases, by separating parts of data structures and processing
and model/layer development.

Some concise tenets for development

* Write unit tests as you go.
* Commit changes, and commit frequently. Write `semantic`_ git commits!
* Formatting is done with ``black``; don't fuss about it 😃
* For new Python dependencies, use `poetry add <package>`.
* For new environment dependencies, use `conda env export -f environment.yml`.

Notes on best practices, particularly regarding CI/CD, can be found in the extensive
documentation for the `Hypermodern Python Cookiecutter`_ repository.

License
-------

Distributed under the terms of the `MIT license`_,
*Naomi* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@laserkelvin`_'s PyTorch Project Cookiecutter, 
a fork of  `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT license: https://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/mimipynb/Agent Naomi/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://Agent Naomi.readthedocs.io/en/latest/usage.html
.. _semantic: https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716
.. _@laserkelvin: https://github.com/laserkelvin

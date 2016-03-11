===============================
Operations Tooling Framework
===============================

This project is a plugable framework for operation related workflows and devops tasks.

Setup
-----

OSX
~~~

Your going to need xcode or some flavour of it that at least has the gcc libs.
If you already have that use homebrew to install python3

    brew install python3

Homebrew will also install pip (pacakge manager), setuptools and venv.

Ubuntu
~~~~~~

Install python3 from the package manager, ubuntu setup for python 2 otb and needs some massaging to get things going.

Windoze
~~~~~~~

TBD

Build
-----

Setup your venv
~~~~~~~~~~~~~~~

Run the relevant script from the `local` dir in this project from the top level of this project. You should end up with a new
directory in your project called `myvenv` that contains the virtual environment for this project.


You might need to run this as sudo. Its going to install the test libs and run the tests. To build the distributable egg

   python3 setup.py develop

At present the tests are managed seperately through make

   make



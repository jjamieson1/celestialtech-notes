pyenv
##########

Date: 2024-12-04 15:09

Status:

Tags:


Install
********

.. code-block:: console

   curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init -)"

**List all the versions you can install**

.. code-block:: console

   pyenv install --list  

**Install a version**

.. code-block:: console

   pyenv install x.x.x

**Make a version global**

.. code-block:: console

   pyenv global x.xx

**Create a virtual env** ( as an example (python2 is just a name))

.. code-block:: console

   pyenv virtualenv 2.7.18 python2

   # using pip2 to install packages

   pip2 install -U <package_name>

**Activate an environment**

.. code-block:: console

   pyenv activate python2

References
**************
https://medium.com/@adocquin/mastering-python-virtual-environments-with-pyenv-and-pyenv-virtualenv-c4e017c0b173

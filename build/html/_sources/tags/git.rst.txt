############
git
############

2024-11-06 10:17

Status: #new

Tags: #coding #source

**********************************
Configure your SSH Key
**********************************

Configure Git with SSH Key

To configure Git to use your SSH key, follow these steps:

**********************************
Step 1: Generate an SSH key
**********************************

If you haven’t already, generate a new SSH key pair using
the ``ssh-keygen`` command. The default location for the key pair
is ``~/.ssh`` on Linux/macOS or ``C:\Users\<YourUsername>\.ssh`` on
Windows.

Example command:

.. code-block:: console

   ssh-keygen -t ed25519 -C "your_email@example.com"

**********************************
Step 2: Copy the public key
**********************************

Copy the contents of the public key file
(``id_ed25519.pub`` or ``id_rsa.pub``) to your clipboard.

***************************************************
Step 3: Add the public key to your GitHub account
***************************************************

Log in to your GitHub account and navigate to your account settings.
Click on “SSH and GPG keys” and then click “New SSH key”. Paste the
contents of your public key into the “Key” field and give it a label
(e.g., “Personal laptop”). Click “Add key”.

***************************************************
Step 4: Configure Git to use the SSH key
***************************************************

On Linux/macOS:

.. code-block:: console

   git config --global ssh.command "ssh -i ~/.ssh/id_ed25519"

On Windows:

.. code-block:: console

   git config --global ssh.command "ssh -i C:\\Users\\YourUsername\\.ssh\\id_ed25519"

Replace ``id_ed25519`` with the actual name of your private key file.

**********************************
Step 5: Test the connection
**********************************

Try connecting to your GitHub repository using the SSH URL:

.. code-block:: console

   git ls-remote --exit-code git@github.com:your_username/your_repo.git

If everything is set up correctly, you should see a list of references
in the remote repository.

***************************************************
What is a Branch and what is “main”
***************************************************

branches are a copy of the main code branch that you can work on, so
that you don’t over write others work. The workflow when creating a new
feature/fix etc…is : 1. Pull the most recent copy of main 2. Create a
branch of that code 3. make/add you changes 4. request a merge back into
main. 5. Reviews check your code through a review. 6. Code is merged
with main, or rejected and the reviews request fixes/changes

**pull a branch**

.. code-block:: console

   git checkout main
   git pull

**create a branch**

.. code-block:: console

   git checkout -b <your feature name> # this will create a branch localy if it does not exist in the remote repository

**when you are done add and commit your code**

.. code-block:: console

   git add <changed files> # I often use the * wildcard to indicate all that has changed.
   git commit -m "A one line description of what changed"
   git push # pushed the repository to github

*****************
Merge Request
*****************

I use the Github website for this part. You can request a merge to main
and select other collaborators to review your code. Once it is approved,
you can perform a merge.

*****************
References
*****************
https://github.com
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

# s3util
A command line tool for s3 with autopath completions and features like vim, cat, recursive restores and batch operations

- ### Path auto completion
Tab completion of s3 paths and buckets

![autocomplete example](/doc/autocomplete.gif "Title")
- ### s3util vim
edit any file on s3 or create new file on s3 using vim

![vim example](/doc/editfileexample.gif "Title")
- ### s3util batch delete
delete multiple directories or file in batch of 1000 objects

![delete example](/doc/deleteexample.gif "Title")

## operations availble

``$ s3util vim <path_to_file>``  to edit file on vim

``$ s3util cat <space_seperated_paths_to_file>`` to print content of file

``$ s3util rm <space_seperated_paths_to_file>`` to delete objects on paths

``$ s3util restore <space_seperated_paths_to_file>`` to restore objects from glacier on paths

``$ s3util ls <space_seperated_paths_to_file>`` to list objects on paths

``$ s3util cp <path1> <path2>`` Copy path1 to path2

``$ s3util mv <path1> <path2>`` Move path1 to path2


- ``--recursive`` command is available for `cat`, `restore`, `rm`, `ls` , `cp` , `mv` to performe operation on all the objects on the path
- `--profile` command can be used to use a particular profile
 ex `s3util --profile <profile_name> <operation> <path> <options>`


## Install Instruction

``$ pip install s3util``

follow below setup for autocompletion according to the terminal you are using (bash, zsh etc)


## For Local development
`` $ git clone https://github.com/karannaoh/s3util.git``

`` $ cd s3util/``

``$ pip install -r requirement.txt``

``$ python3 setup.py install ``

``$ python3 setup.py sdist bdist_wheel ``

``$ pip install s3util ``



## For autocompletion to work, 

For bash,

`` $ activate-global-python-argcomplete``

and add 

``eval "$(register-python-argcomplete s3util)"`` 

in .bashrc file

For zsh

enable `bashcompinit`

``$ autoload -U bashcompinit``

``$ bashcompinit``

and add 

``eval "$(register-python-argcomplete s3util)"`` 

in .zshrc file

follow https://github.com/kislyuk/argcomplete for other programs
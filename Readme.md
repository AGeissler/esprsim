# esprsim

## Introduction
The 'esprsim' package provides an interface for running ESP-r using
Python scripts. There is an example how such an automation script can
be set up in the example folder.

## Installing esprsim
### Step One
Clone the Gitlab repository from 'git@gitlab.fhnw.ch:GruppeBau/esprsim.git'
to your usual git repository directory.

### Step Two
If your ESP-r project already has a Python virtual environment(or if you
use a central Python installation and wish to add this package to it), 
jump to step three. Otherwise:

Set up a virtual Python environment for your ESP-r project, ideally
in '<project path>', which is either the ESP-r project path if this is 
'stand alone' or the path of the project of which ESP-r files are in 
a subdirectory. The following assumes you are working in a console
window.

    1. Create virtual environment by 
        <project path>$ python3 -m venv env (evironment name is name arbitrary)
        
    2. Activate the virtual environment by 
        Windows    : <project_path>$ .\env\Scripts\activate”
        MacOS/Linux: <project_path>$ source env/bin/activate
        
    3. The prompt should look like this: “(env) <project_path> $ ”

    4. Run 
        pip install --upgrade pip
        pip install wheel
        pip install setuptools

Note: to avoid clutter in git "changed files" tracking, add the
environment subdirectory to .gitignore of the project.

### Step three
In the console with active environment from step two, change to the 
source directory of esprsim and issue the command

    $ pip install .

That's it. Now, esprsim should be available in your project-specific 
virtual environment every time you activate it.

## Usage example
The subdirectory 'example' contains a 'real world' example using the
functionality of the esprsim package. 

The example requires an ESP-r installation @ version 13.3.15.


## Contribution
If any functionality you desire is missing, feel free to extend the code.
Please contact the maintainer to get developer access to the repository.


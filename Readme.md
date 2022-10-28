# esprsim

## Introduction
The 'esprsim' package provides an interface to running ESP-r 
using Python scripts. There is an example how such an automation
script can be set up in the examples folder.

## Installing esprsim
### Step One
Clone the Gitlab repository from 'git@gitlab.fhnw.ch:GruppeBau/esprsim.git'
to your usual git project directory.

### Step Two
If your ESP-r project already has a Python virtual environment, jump to step
three. Otherwise:

Set up a virtual Python environment for your ESP-r project, ideally
in '<project path>', which is either the ESP-r project path if this is 
'stand alone' or the path of the project of which ESP-r files are in 
a subdirectory.

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

### Step three
Change to the source directory of epsim and issue the command

    $ pip install .

Thats it. Now, esprsim should be available in your project-specific virtual
environment every time you activate it.

## Usage example
The subdirectory 'example' contains a 'Real world' example using the
functionality of the epsim package. 

The example requires an ESP-r installation @ version 13.3.15.


## Contribution
If any functionality you desire is missing, feel free to extend the code.
Please contact the maintainer to get developer access to the repository.


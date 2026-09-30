<!--
SPDX-FileCopyrightText: 2026 Achim Geissler <achim.geissler@acatalepsy.ch>
SPDX-License-Identifier: GPL-3.0-or-later
-->
# esprsim

[![REUSE status](https://api.reuse.software/badge/github.com/AGeissler/esprsim)](https://api.reuse.software/info/github.com/AGeissler/esprsim)

## Introduction
The 'esprsim' package provides an interface for running [ESP-r](https://www.strath.ac.uk/research/energysystemsresearchunit/applications/esp-r/) using Python scripts. Therefore, a pre-requisite for using this package is an installed version of ESP-r on the computer. 

> [!WARNING]
> The package is tested with version 13.3.17. The scripts use ``mode -text`` for model manipulation, any changes in ESP-r concerning text mode in earlier or later versions may lead to errors.

There are examples of how automation of ESP-r simulations can be set up in the examples folder.

## Installing esprsim
### Step One
Clone this repository to your usual git repository directory.

### Step Two
If your ESP-r project already has a Python virtual environment(or if you use a central
Python installation and wish to add this package to it), jump to step three. Otherwise:

Set up a virtual Python environment for your ESP-r project, ideally in '<project path>',
which is either the ESP-r project path if this is 'stand alone' or the path of the
project of which ESP-r files are in a subdirectory. The following assumes you are working
in a console window.

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

Note: to avoid clutter in git "changed files" tracking, add the environment subdirectory
to .gitignore of the project.

### Step Three
In the console with active environment from step two, change to the source directory of
esprsim and issue the command

    $ pip install .

That's it. Now, esprsim should be available in your project-specific virtual environment
every time you activate it.

## Usage example
The subdirectory 'examples' contains a simple and a more detailed example model and examples of increasing complexity using the functionality of the 'esprsim' package.

## Contribution
Feel free to extend the code via a fork of the repository for any missing functionality you desire and submit a pull request to the maintainer.

## Maintainer
Author and maintainer is achim.geissler@acatalepsy.ch.

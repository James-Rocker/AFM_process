# AFM_process
## Pre-requisites

You will need a copy of python 3. Ideally 3.7.10 onwards as specified in the python-version config file, but it's not essential
[Link to download python](https://www.python.org/downloads/).

Use a 64 bit version if possible. It'll be faster.

Make sure on installation of python to check `Add Python to PATH`. This will allow you to use commands in the commandline.

## Setup

Navigate to this project folder in cmd or bash
Create a venv environment with `python3 -m venv ./venv`  
Activate the virtual environment with `source venv/bin/activate`  
From there you have an independent project space to start install modules  

To install the required modules, use `pip install -r requirements.txt`  
If you have installed more modules with pip install. Update the requirements file with `pip freeze > requirements.txt`

## Where to put my boxfiles

In the `HepG2/curves` folder within this project

## To run

In your activated virtual environment shell, use `python3 main.py`

## Replacing graphs

You don't need to worry about that, just place your box text files in the `HepG2/curves` folder then run. This will overwrite
existing graphs in the output directory 

## Adding code

If you plan on adding code, please use the command `black .` to auto lint when it when you are done (saves arguments and makes things more readable)

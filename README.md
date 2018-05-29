# Pycon Asia 2018
This is a supplementary python scripts for my presentation for Pycon Asia 2018 in Singapore. The presentation is titled "Maintaining robust and maintainable concurrent program".

## Instructions
1. The python scripts were written and tested using Python 3.6.4 version.
2. There is only 1 requirement (colorama) specified in the requirements.txt. This is to visualize the kue lapis.
3. To run the application:
    3.1. first create a virtual env: `python -m venv .venv`
    3.2. source the environment: `source .venv/bin/activate`
    3.3. install the requirement: `pip install -r requirements.txt`
    3.4. run any script, e.q. `python kue_lapis.py`

## The scripts
***

### Script kue_lapis.py
This script simulates the creation of kue lapis for both sequential and multi threaded approach.

### Script kue_lapis_multi_process.py
This script simulates the creation of kue lapis using multi processing approach.


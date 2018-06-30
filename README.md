# Learning Selenium and BDD in python

Code examples for learning combination of Selenium and Behaviour-Driven Development (BDD) in python.

Behave directory structure:

```
/features
    *.feature
    environment.py
    /steps
        *.py
```
`*.feature` files should have identical name with `*.py*` inside `/steps` directory

Running cucumber script from terminal:

`behave --no-capture features/*.feature`

### Required libraries:
* Selenium Python
* Behave
* Chromedriver

### Install libraries
Run this command on terminal: `pip install -r requirements.txt`

### Get chromedriver
Download it here: http://chromedriver.chromium.org/downloads

Add it inside the project directory
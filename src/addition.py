# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

# For GitHub actions 
# Anytime there's a new commit or change to this file, Github actions should check out this program
# by checking the python code and then create a python env (to verify the code on python version 3.8 and 3.9)
# because there's no python server configured here (unlike Jenkins where you have them pre-configured)
# either using Docker containers or else you create your worker nodes in which you install python server
# (inside a ubuntu-latest docker image) and set up all the required env, 
# and finally you run this program and then run the test.
    
# So all these info or tasks (jobs) will be interpreted in Github actions file for it to execute
# i.e. first-actions.yml. You can check via the yellow small button beside the commit id by clicking on it 
# in your GitHub repo.

import os
from nose.tools import assert_equal, assert_true
import stat
import shutil
import pandas as pd

import markdown

def test_timestamp():
    try:
        assert_true(os.path.exists("./timestamp.txt"))
        print("timestamp.txt file exists")
    except:
        print("timestamp.txt files does not exist")

def display_bc(fname="business_card.md"):
    from IPython.display import HTML, display
    try:
        with open(fname) as f0:
            bc = f0.read()
        display(HTML(markdown.markdown(bc)))
    except:
        print("Could not read business card")

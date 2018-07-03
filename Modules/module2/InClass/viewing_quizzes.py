from nose.tools import assert_equal
import os

def oct15(ocount=-1):
    with open(os.path.join(os.path.expanduser("~"),"DATA","Misc", "obits.txt")) as f0:
        obits = f0.read()
    try:
        assert_equal(obits.count("Oct. 15"), ocount)
        print("October 15 counted correctly")
    except:
        print("October 15 NOT counted correctly")



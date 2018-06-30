import os
from nose.tools import assert_equal, assert_true
import stat
import shutil
import pandas as pd

def nci_ftp_quiz():

    try:
        assert_true(os.path.exists("/home/jovyan/work/nci/var_citations.txt"))
        print("var_citations.txt exist in the correct location")
        try:
            df1 = pd.read_table("/home/jovyan/work/nci/var_citations.txt")
            df2 = pd.read_table("ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/var_citations.txt")
            assert_true(df2.equals(df1))
            print("var_citations.txt read correctly")
        except:
            print("var_citations.txt does not exist in the correct location")

    except:
        print("var_citations.txt not red correctly")



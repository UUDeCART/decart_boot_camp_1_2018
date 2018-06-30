from nose.tools import assert_equal

def bp_hr_ge200(answer=-1):
    try:
        assert_equal( 39, answer)
        print('number of patients identified correctly.')
    except:
        print('number of patients NOT identified correctly.')

def mitral_files(answer=-1):
    try:
        assert_equal( 2, answer)
        print('number of mitral audible files identified correctly.')
    except:
        print('number of mitral audible files NOT identified correctly.')

def wave_files(answer=-1):
    try:
        assert_equal( 11, answer)
        print('number of WAVE audible files identified correctly.')
    except:
        print('number of WAVE audible files NOT identified correctly.')

def find_10k_files(answer=-1):
    try:
        assert_equal( 71, answer)
        print('number of *.txt files larger than 10k identified correctly.')
    except:
        print('number of *.txt files larger than 10k NOT identified correctly.')



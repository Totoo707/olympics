import pytest
import argparse
from olympics.__main__ import main

def test_main_countries():
    argv = ['countries']
    main(argv)

def test_main_collective():
    argv = ['collective']
    main(argv)

def test_main_individual():
    argv = ['individual']
    main(argv)

def test_main_invalid_top():
  with pytest.raises(argparse.ArgumentTypeError):
        argv = ['individual', '--top', '-1']
        main(argv)
 


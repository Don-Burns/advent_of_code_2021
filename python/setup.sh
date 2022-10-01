#!/bin/sh
prefix="day_"
for i in {3..25}
do
    f_path=$prefix$i
    code_path=$f_path/${f_path}.py
    test_path=$f_path/test_${f_path}.py
    mkdir $f_path
    touch $code_path
    touch $test_path
    echo "#!/usr/bin/env python3
import pandas as pd

input_file = 'validation_input.txt'

def parse_input():
    pass

class Day${i}:
    def __init__(self) -> None:
        self.input = parse_input(input_file)

def main():
    pass

if __name__ == '__main__':
    input_file = 'input.txt'
    main()
" >> $code_path
    
    echo "#!/usr/bin/env python3
import pytest
import pandas as pd
from random import randint
from ${f_path} import Day$i, parse_input
class TestDay:

    def test_input(self, input_path = 'validation_input.txt'):
        ind = randint(0,5)
        assert pd.read_csv(input_path, header=None).loc[ind,0] == parse_input(input_path).loc[ind,0]" >> $test_path

    touch $f_path/validation_input.txt
    touch $f_path/input.txt
done

#python dependencies
# pip install pipenv
# pipenv install dependencies.txt
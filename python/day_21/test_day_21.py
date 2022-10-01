#!/usr/bin/env python3
import pytest
import pandas as pd
from random import randint
from day_21 import Day21, parse_input
class TestDay:

    def test_input(self, input_path = 'validation_input.txt'):
        ind = randint(0,5)
        assert pd.read_csv(input_path, header=None).loc[ind,0] == parse_input(input_path).loc[ind,0]

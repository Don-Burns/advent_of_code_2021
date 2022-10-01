#!/usr/bin/env python3
import pytest
import pandas as pd
from day_1 import Day1, parse_input

input_file = "validation_input.txt"

class TestDay:

    def setUp(self):
        self.test_input_path = "validation_input.txt"

    def test_input_parser(self):
        # assert self.test_input == parse_input(self.test_input_path)
        assert len(pd.read_csv("validation_input.txt", header=None))== len(parse_input("validation_input.txt"))


    def test_should_count_incrementing_values(self):
        assert 7 == Day1().count_increments()

    def test_should_count_sliding_window_increase(self):
        assert 5 == Day1().count_window_increase()


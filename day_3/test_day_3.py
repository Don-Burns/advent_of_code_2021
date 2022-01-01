#!/usr/bin/env python3
import pytest
import pandas as pd
from day_3 import Day3, parse_input

class TestDay:

    def test_input(self, input_path = 'validation_input.txt'):
        assert '00100' == parse_input(input_path).loc[0,0]

    def test_binary_conversion(self):
        assert Day3().binary_to_decimal('10110') == 22

    def test_should_return_most_common_bit_in_each_position_of_input_array(self):
        assert '10110' == Day3().gamma_binary
    
    def test_should_return_least_common_bit_in_each_position_of_input_array(self):
        assert '01001' == Day3().epsilon_binary

    def test_should_return_converted_gamma_decimal(self):
        assert 22 == Day3().gamma_decimal
    
    def test_should_return_converted_epsilon_decimal(self):
        assert 9 == Day3().epsilon_decimal
    
    def test_should_return_power_consumption(self):
        assert 198 == Day3().power_consumption

    def test_find_o2_generator_binary(self):
        assert '10111' == Day3().o2_binary

    def test_find_co2_generator_binary(self):
        assert '01010' == Day3().co2_binary

    def test_find_o2_generator_decimal(self):
        assert 23 == Day3().o2_decimal

    def test_find_co2_generator_decimal(self):
        assert 10 == Day3().co2_decimal
    
    def test_life_support_rating(self):
        assert 230 == Day3().life_support_rating

    
    
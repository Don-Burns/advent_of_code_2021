#!/usr/bin/env python3
import pytest
import pandas as pd
from random import randint
from day_2 import Day2, Day2Pt2, parse_input
class TestDayPart1:

    def test_input(self, input_path = 'validation_input.txt'):
        ind = randint(0,5)
        assert pd.read_csv(input_path, header=None).loc[ind,0] == parse_input(input_path).loc[ind,0]

##PART 1
    def test_horizontal_position(self):
        submarine = Day2()
        submarine.move()
        hor_pos = submarine.x_pos
        assert hor_pos == 15

    def test_depth(self):
        submarine = Day2()
        submarine.move()
        depth = submarine.depth
        assert depth == 10
    
    def test_multiply_postion_values(self):
        submarine = Day2()
        submarine.move()
        assert submarine.x_pos * submarine.depth == 150

class TestDayPart2:
##PART2
    def test_part_2_horizontal_position(self):
        submarine = Day2Pt2()
        submarine.move()
        assert submarine.x_pos == 15

    
    def test_part_2_depth(self):
        submarine = Day2Pt2()
        submarine.move()
        assert submarine.depth == 60

    

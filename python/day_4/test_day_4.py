#!/usr/bin/env python3
import pytest
import pandas as pd
from random import randint
from day_4 import Day4

new_bingo = Day4()
bingo = Day4()
bingo.run_game()

class TestDay:

    def test_input_numbers(self):
        ind = randint(0,5)
        input_list = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
        assert input_list[ind] == bingo.number_list[ind]

    def test_input_cards(self):
        assert 8 == new_bingo.boards["board_0"][1][0]

    def test_board_marking(self):
        new_bingo.mark_boards(number=8)
        assert True == new_bingo.marking_boards["board_0"][1][0]

    def test_getting_the_winning_row(self):
        assert [14, 21, 17, 24, 4] == bingo.winning_boards[0]["values"]

    def test_last_called_num(self):
        assert 24 == bingo.winning_boards[0]["last_called_num"]

    def test_winning_sum(self):
        assert 188 == bingo.winning_boards[0]["unmarked_sum"]

    def test_final_score(self):
        assert 4512 == bingo.winning_boards[0]["final_score"]

    #pt2
    def test_last_winning_board_last_call_num(self):
        assert 13 == bingo.winning_boards[-1]["last_called_num"]

    def test_last_winning_board_winning_sum(self):
        assert 148 == bingo.winning_boards[-1]["unmarked_sum"]

    def test_last_winning_board_final_score(self):
        assert 1924 == bingo.winning_boards[-1]["final_score"]

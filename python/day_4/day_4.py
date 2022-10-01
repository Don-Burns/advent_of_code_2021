#!/usr/bin/env python3
import pandas as pd
import re
from copy import deepcopy
from pprint import pprint

input_file = 'validation_input.txt'

class Day4:
    def __init__(self) -> None:
        self.input = self.parse_input(input_file)
        self.number_list = self.input["number_list"]
        self.boards = {i : val for i, val in self.input.items() if i != "number_list"}
        self.marking_boards = self.generate_marking_boards()
        self.last_called_num = 0
        self.winner = None
        self.initalise_winner_dict()
        self.winning_boards = []
        

    def parse_input(self, input_file:str) -> dict:
        output = {}
        with open(input_file, 'r') as f:
            input = f.read().split('\n\n')
        output["number_list"] = [int(x) for x in input[0].split(",")]
        for i, val in enumerate(input[1:]):
            tmp = [x for x in val.split("\n")]
            tmp = [re.split("\s+", x.strip()) for x in tmp]
            output[f"board_{i}"] = [list(map(int,y)) for y in tmp]
        return output
    
    def initalise_winner_dict(self) -> dict:
        self.winner =   {
            "board" : "",
            "winner" : False,
            "winning_axis" : "", #x/y
            "values" : [],
            "unmarked_sum" : 0,
            "final_score" : 0,
            "last_called_num" : None
        }

    def generate_marking_boards(self) -> dict:
        boards = deepcopy(self.boards)
        for key, val in boards.items():
            boards[key]= [list(map(lambda x: False,y)) for y in val]
        return boards

    def index_of_number(self, number:int, board:list) -> tuple:
        j = None
        for i, val in enumerate(board):
            try:
                j = val.index(number)
            except ValueError:
                continue
            if j is not None:
                return(i,j)
        if j is None:
            # print(f"{number} not found in board")
            return None

    def mark_boards(self, number:int) -> None:
        for key, board in self.boards.items():
            ind = self.index_of_number(number, board)
            if ind is not None:
                self.marking_boards[key][ind[0]][ind[1]] = True

    def check_for_winning_rows(self, board_name:str) -> None:
        board = self.boards[board_name]
        marking_board = self.marking_boards[board_name]
        for i, row in enumerate(marking_board):
            if sum(row) == len(row):
                winning_row = board[i]
                self.winner["winner"] = True
                self.winner["axis"] = "x"
                self.winner["values"] = winning_row
                self.winner["unmarked_sum"] = self.sum_unmarked_values(board, marking_board)
                self.winner["board"] = board_name
                return

    def check_for_winning_cols(self, board_name:str) -> None:
        marking_board = self.marking_boards[board_name]
        board = self.boards[board_name]
        num_cols = len(marking_board)
        for col_ind in range(num_cols):   
            _ = []
            _col = []
            for i, row in enumerate(marking_board):
                _.append(row[col_ind])
                _col.append(board[i][col_ind])
            col_sum = sum(_)
            if col_sum == num_cols:
                self.winner["winner"] = True
                self.winner["axis"] = "y"
                self.winner["values"] = _col
                self.winner["unmarked_sum"] = self.sum_unmarked_values(board, marking_board)
                self.winner["board"] = board_name
                return
    
    def sum_unmarked_values(self, board:list, marking_board:list) -> int:
        unmarked_values = []
        for i, row in enumerate(marking_board):
            for j, marked in enumerate(row):
                if marked == False:
                    unmarked_values.append(board[i][j])
        return sum(unmarked_values)

    def find_winner(self) -> None:
        """
        finds winning row or col
        """
        for key in self.marking_boards.keys():
            self.check_for_winning_rows(key)
            if self.winner["winner"] == True:
                break
            self.check_for_winning_cols(key)
            if self.winner["winner"] == True:
                break
        self.winner["final_score"] = self.last_called_num * self.winner["unmarked_sum"]
        return
    
    def save_winning_board(self) -> None:
        self.winner["last_called_num"] = self.last_called_num
        self.winning_boards.append(deepcopy(self.winner))
        board_name = self.winner["board"]
        del self.boards[board_name]
        del self.marking_boards[board_name]
        self.initalise_winner_dict()
        

    def run_game(self) -> None:
        for i in self.number_list:
            self.last_called_num = i
            self.mark_boards(i)
            self.find_winner()
            if self.winner["winner"] == True:
                self.save_winning_board()
                # print(len(self.boards.keys()))
                # print(f"number of winners = {len(self.winning_boards)} \nnum remaining = {len(self.boards.keys())}")
                if len(self.boards.keys()) == 0: break
        # if len(self.boards) != 0:
        #     raise Exception("All boards were not marked complete, despite all numbers being called")
        return

def main():
    bingo = Day4()
    # pprint(bingo.boards)
    bingo.run_game()
    # print(bingo.winner)
    # print(bingo.last_called_num)
    # pprint(bingo.winning_boards[-1])
    #pt 1 
    first_winner_score = bingo.winning_boards[0]["final_score"]
    print(f"total score for the first winning board is {first_winner_score}")

if __name__ == '__main__':
    input_file = 'input.txt'
    main()


#!/usr/bin/env python3
import pandas as pd

input_file = "validation_input.txt"


def parse_input(file_path):
    return pd.read_csv(file_path, header=None)

class Day1():
       
    def __init__(self) -> None:
        self.input = parse_input(input_file)
    
    def count_increments(self):
        count = 0
        col = self.input.loc[:,0]
        for i, val in enumerate(col):
            if i == 0:
                continue
            prev_val = col[i-1]
            if prev_val < val:
                count += 1
        return count
    
    def count_window_increase(self):
        count = 0
        col = self.input.loc[:,0].values
        for i, val in enumerate(col):
            if i <= 1 or i == len(col):
                continue
            prev_sum = sum(col[i-2:i+1])
            cur_sum = sum(col[i-1:i+2])
            if prev_sum < cur_sum:
                count+=1
        return count


def main():
    obj = Day1()
    print(f"count of increase of previous value = {obj.count_increments()}")
    print(f"count of increase when using sliding window of 3 values summed = {obj.count_window_increase()}")

if __name__ == "__main__":
    input_file = "input.txt"
    main()




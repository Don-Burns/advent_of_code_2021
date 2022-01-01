#!/usr/bin/env python3
import pandas as pd

input_file = 'validation_input.txt'

def parse_input(file_path):
    return pd.read_csv(input_file, header=None)

class Day2:
    def __init__(self) -> None:
        self.input = parse_input(input_file).loc[:,0]
        self.depth = 0
        self.x_pos = 0
        self.direction_map = {
            "forward" : ("x_pos", 1),
            # "backward" : ("x_pos", -1),
            "up" : ("depth", -1),
            "down" : ("depth", 1)
        }

    def move(self):
        for i in self.input:
            direction, val = i.split(' ')
            val = int(val)
            pos, multiplier = self.direction_map[direction]
            if pos == "x_pos":
                self.x_pos += val * multiplier
            if pos  == "depth":
                self.depth += val * multiplier
        return 0

class Day2Pt2:
    def __init__(self) -> None:
        self.input = parse_input(input_file).loc[:,0]
        self.depth = 0
        self.x_pos = 0
        self.aim = 0
        self.direction_map = {
            "forward" : ("x_pos", 1),
            # "backward" : ("x_pos", -1),
            "up" : ("depth", -1),
            "down" : ("depth", 1)
        }

    def move(self):
        for i in self.input:
            direction, val = i.split(' ')
            val = int(val)
            pos, multiplier = self.direction_map[direction]
            val_added = val * multiplier
            if pos == "x_pos":
                self.x_pos += val_added
                self.depth += self.aim * val_added
            if pos  == "depth":
                # self.depth += val_added
                self.aim += val_added

        return 0


def main():
    print("--------------------------------------------------\nrunning part 1:")
    sub = Day2()
    sub.move()
    print(f"submarine depth = {sub.depth}\n submarine horizontal positon = {sub.x_pos}")
    print(f"Position values multiplied together = {sub.depth * sub.x_pos}")

    print("--------------------------------------------------\nrunning part 2:")
    sub = Day2Pt2()
    sub.move()
    print(f"submarine depth = {sub.depth}\n submarine horizontal positon = {sub.x_pos}")
    print(f"Position values multiplied together = {sub.depth * sub.x_pos}")

if __name__ == '__main__':
    input_file = 'input.txt'
    main()


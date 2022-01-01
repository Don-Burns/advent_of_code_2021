#!/usr/bin/env python3
import pandas as pd
from copy import deepcopy

input_file = 'validation_input.txt'

def parse_input(file_path:str):
    return pd.read_csv(file_path, header=None, dtype=str)

class Day3:
    def __init__(self) -> None:
        self.input = self.input_to_binary()
        self.gamma_binary = self.get_gamma_rate()
        self.epsilon_binary = self.get_epsilon_rate()
        self.gamma_decimal = self.binary_to_decimal(self.gamma_binary)
        self.epsilon_decimal = self.binary_to_decimal(self.epsilon_binary)
        self.power_consumption = self.gamma_decimal * self.epsilon_decimal
        #pt2
        self.o2_binary = self.get_o2_binary()
        self.co2_binary = self.get_co2_binary()
        self.o2_decimal = self.binary_to_decimal(self.o2_binary)
        self.co2_decimal = self.binary_to_decimal(self.co2_binary)
        self.life_support_rating = self.co2_decimal * self.o2_decimal

    def input_to_binary(self): #TODO refactor this
        input = parse_input(input_file).loc[:,0]
        output = []
        for i in input:
            output.append(i)
        return output
    
    def binary_to_decimal(self, binary:str) -> int:
        binary = '0b'+binary
        return int(binary, 2)

    def get_most_common_bit(self, bin_list:list) -> str:
        output = ''
        bin_len = len(bin_list[0])
        list_ent = len(bin_list)
        for i in range(bin_len):
            col_sum = 0 
            for j in bin_list:
                col_sum += int(j[i])
            if col_sum < (list_ent/2):
                insert_val = 0
            else:
                insert_val = 1
            output += str(insert_val)
        return output

    def get_least_common_bit(self, bin_list:list) -> str:
        output = ''
        bin_len = len(bin_list[0])
        list_ent = len(bin_list)
        for i in range(bin_len):
            col_sum = 0 
            for j in bin_list:
                col_sum += int(j[i])
            if col_sum >= (list_ent/2):
                insert_val = 0
            else:
                insert_val = 1
            output += str(insert_val)
        return output


    def get_gamma_rate(self) -> str:
        return self.get_most_common_bit(self.input)

    def flip_binary(self, binary) -> str:
        output = ''
        for i in binary:
            if i == '0':
                insert_val = '1'
            else:
                insert_val = '0'
            output += insert_val
        return output

    def get_epsilon_rate(self) -> str:
        # return self.flip_binary(self.gamma_binary)
        return self.get_least_common_bit(self.input)


    def get_o2_binary(self):
        output = deepcopy(self.input)
        bin_pos = 0
        while len(output) > 1:
            del_list = []
            bit = self.get_most_common_bit(output)[bin_pos]
            for i, val in enumerate(output):
                if val[bin_pos] != bit:
                    del_list.append(i)
            for i in reversed(del_list):
                del output[i]
            bin_pos += 1
        return output[0]
    
    def get_co2_binary(self):
        output = deepcopy(self.input)
        bin_pos = 0
        while len(output) > 1:
            del_list = []
            bit = self.get_least_common_bit(output)[bin_pos]
            for i, val in enumerate(output):
                if val[bin_pos] != bit:
                    del_list.append(i)
            for i in reversed(del_list):
                del output[i]
            bin_pos += 1
        return output[0]
            

def main():
    obj = Day3()
    print(f"power consumption = {obj.power_consumption}")
    print(f"life support rating = {obj.life_support_rating}")


if __name__ == '__main__':
    input_file = 'input.txt'
    main()



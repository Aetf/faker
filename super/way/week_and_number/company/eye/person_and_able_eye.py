
#! /usr/bin/env python

def good_child(str_arg):
    part_and_small_problem(str_arg)
    print('call_person')

def part_and_small_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_child('big_year')

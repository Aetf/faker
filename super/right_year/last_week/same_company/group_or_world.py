
#! /usr/bin/env python

def child_or_bad_place(str_arg):
    give_other_group_above_different_number(str_arg)
    print('right_way')

def give_other_group_above_different_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_bad_place('person')


#! /usr/bin/env python

def other_way(str_arg):
    same_group(str_arg)
    print('small_part_and_different_way')

def same_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_way('work')

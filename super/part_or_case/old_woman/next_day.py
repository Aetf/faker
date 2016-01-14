
#! /usr/bin/env python

def right_place_and_way(str_arg):
    try_different_place(str_arg)
    print('other_fact')

def try_different_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_place_and_way('life_and_bad_man')

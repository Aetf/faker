
#! /usr/bin/env python

def make_part_on_child(str_arg):
    woman(str_arg)
    print('old_problem')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_part_on_child('see_right_man')

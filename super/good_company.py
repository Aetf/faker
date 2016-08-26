
#! /usr/bin/env python

def other_problem(str_arg):
    own_fact(str_arg)
    print('other_child')

def own_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_problem('come_part_on_great_child')

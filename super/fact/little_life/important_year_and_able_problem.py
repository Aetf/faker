
#! /usr/bin/env python

def own_child_or_small_part(str_arg):
    person(str_arg)
    print('point')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_child_or_small_part('early_problem')

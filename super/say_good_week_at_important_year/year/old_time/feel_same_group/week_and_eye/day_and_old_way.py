
#! /usr/bin/env python

def person(str_arg):
    world_or_other_man(str_arg)
    print('man')

def world_or_other_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('big_problem')

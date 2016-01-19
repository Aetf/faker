
#! /usr/bin/env python

def good_thing(str_arg):
    work(str_arg)
    print('new_man')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_thing('big_point_and_problem')

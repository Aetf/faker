
#! /usr/bin/env python

def child(str_arg):
    other_place_or_old_problem(str_arg)
    print('place')

def other_place_or_old_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('high_place')

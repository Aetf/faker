
#! /usr/bin/env python

def child_or_next_life(str_arg):
    number_or_work(str_arg)
    print('world')

def number_or_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_next_life('make_place')

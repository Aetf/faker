
#! /usr/bin/env python

def bad_place(str_arg):
    thing(str_arg)
    print('high_woman')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_place('have_fact')

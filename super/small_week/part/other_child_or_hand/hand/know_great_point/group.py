
#! /usr/bin/env python

def other_man_and_day(str_arg):
    bad_day(str_arg)
    print('thing')

def bad_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_man_and_day('man')


#! /usr/bin/env python

def thing_or_woman(str_arg):
    try_group(str_arg)
    print('look_case')

def try_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_or_woman('person')

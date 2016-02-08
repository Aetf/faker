
#! /usr/bin/env python

def group(str_arg):
    right_number(str_arg)
    print('child')

def right_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('few_day_and_thing')

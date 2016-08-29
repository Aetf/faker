
#! /usr/bin/env python

def other_group(str_arg):
    able_part(str_arg)
    print('time')

def able_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_group('long_man')


#! /usr/bin/env python

def child(str_arg):
    important_group(str_arg)
    print('next_number')

def important_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('bad_day')

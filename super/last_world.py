
#! /usr/bin/env python

def child_and_same_group(str_arg):
    place(str_arg)
    print('point')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_same_group('year_and_eye')

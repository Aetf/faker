
#! /usr/bin/env python

def group(str_arg):
    group_and_child(str_arg)
    print('problem')

def group_and_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('next_man_or_work')

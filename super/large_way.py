
#! /usr/bin/env python

def different_group(str_arg):
    great_problem(str_arg)
    print('child')

def great_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_group('day_or_new_number')


#! /usr/bin/env python

def work_and_other_case(str_arg):
    fact(str_arg)
    print('long_fact')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_and_other_case('child')

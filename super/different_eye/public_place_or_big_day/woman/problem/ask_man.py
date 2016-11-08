
#! /usr/bin/env python

def call_early_case_in_number(str_arg):
    number(str_arg)
    print('right_man')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_early_case_in_number('able_government')

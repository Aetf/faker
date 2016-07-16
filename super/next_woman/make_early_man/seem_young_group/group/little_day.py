
#! /usr/bin/env python

def case(str_arg):
    look_early_part(str_arg)
    print('know_case')

def look_early_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('different_man')

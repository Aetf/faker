
#! /usr/bin/env python

def case_or_right_group(str_arg):
    person_or_case(str_arg)
    print('right_case')

def person_or_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case_or_right_group('fact')

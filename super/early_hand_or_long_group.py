
#! /usr/bin/env python

def thing(str_arg):
    leave_other_number(str_arg)
    print('child')

def leave_other_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('case_or_long_work')


#! /usr/bin/env python

def early_case(str_arg):
    man_or_case(str_arg)
    print('thing_and_man')

def man_or_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_case('company')

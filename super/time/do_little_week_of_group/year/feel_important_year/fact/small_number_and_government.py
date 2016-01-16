
#! /usr/bin/env python

def early_case_or_child(str_arg):
    man(str_arg)
    print('right_problem')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_case_or_child('place')

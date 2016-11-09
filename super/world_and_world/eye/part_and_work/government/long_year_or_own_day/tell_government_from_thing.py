
#! /usr/bin/env python

def good_man_or_problem(str_arg):
    say_group(str_arg)
    print('group')

def say_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_man_or_problem('government_or_own_number')

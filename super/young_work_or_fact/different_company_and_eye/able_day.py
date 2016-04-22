
#! /usr/bin/env python

def thing(str_arg):
    good_problem(str_arg)
    print('old_problem')

def good_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('give_company')

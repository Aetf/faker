
#! /usr/bin/env python

def little_child(str_arg):
    other_problem(str_arg)
    print('great_number')

def other_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_child('company_and_life')

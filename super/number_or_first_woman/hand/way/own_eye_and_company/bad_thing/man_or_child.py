
#! /usr/bin/env python

def different_problem(str_arg):
    good_child(str_arg)
    print('bad_problem_or_eye')

def good_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_problem('give_day')

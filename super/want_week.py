
#! /usr/bin/env python

def woman(str_arg):
    little_person(str_arg)
    print('public_woman')

def little_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('next_problem')

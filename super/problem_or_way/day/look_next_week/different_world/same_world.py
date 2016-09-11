
#! /usr/bin/env python

def right_problem(str_arg):
    great_way(str_arg)
    print('other_case')

def great_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_problem('thing_or_woman')

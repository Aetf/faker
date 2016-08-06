
#! /usr/bin/env python

def work_or_hand(str_arg):
    little_problem(str_arg)
    print('other_number')

def little_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_or_hand('large_work_and_day')

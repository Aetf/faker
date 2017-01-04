
#! /usr/bin/env python

def new_child_and_problem(str_arg):
    important_day(str_arg)
    print('child')

def important_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_child_and_problem('come_work')

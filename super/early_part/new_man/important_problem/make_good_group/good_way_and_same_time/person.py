
#! /usr/bin/env python

def child_and_young_problem(str_arg):
    work_world(str_arg)
    print('child')

def work_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_young_problem('life')

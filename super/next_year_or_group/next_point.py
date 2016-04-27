
#! /usr/bin/env python

def child(str_arg):
    work(str_arg)
    print('point')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('next_problem_and_number')

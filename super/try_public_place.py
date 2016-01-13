
#! /usr/bin/env python

def way(str_arg):
    thing(str_arg)
    print('child')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    way('know_problem_after_public_day')

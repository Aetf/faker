
#! /usr/bin/env python

def work(str_arg):
    problem_or_large_thing(str_arg)
    print('call_different_group')

def problem_or_large_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('next_week')

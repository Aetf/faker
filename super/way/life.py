
#! /usr/bin/env python

def high_work(str_arg):
    thing(str_arg)
    print('take_work_at_next_case')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    high_work('life')

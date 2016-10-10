
#! /usr/bin/env python

def go_long_problem(str_arg):
    call_good_way(str_arg)
    print('next_hand')

def call_good_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_long_problem('thing')

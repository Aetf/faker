
#! /usr/bin/env python

def call_time(str_arg):
    early_fact(str_arg)
    print('world')

def early_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_time('problem_or_hand')

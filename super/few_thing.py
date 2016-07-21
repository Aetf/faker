
#! /usr/bin/env python

def man(str_arg):
    call_next_place_over_last_work(str_arg)
    print('hand')

def call_next_place_over_last_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('little_fact')

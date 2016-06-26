
#! /usr/bin/env python

def work(str_arg):
    world(str_arg)
    print('make_small_fact_on_next_world')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('case')

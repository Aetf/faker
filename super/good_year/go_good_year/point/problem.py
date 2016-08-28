
#! /usr/bin/env python

def world(str_arg):
    person(str_arg)
    print('world')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('say_good_fact_under_small_time')

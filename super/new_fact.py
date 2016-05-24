
#! /usr/bin/env python

def last_work(str_arg):
    tell_fact_to_world(str_arg)
    print('important_thing')

def tell_fact_to_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    last_work('fact')

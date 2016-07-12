
#! /usr/bin/env python

def child(str_arg):
    important_fact_or_large_year(str_arg)
    print('other_thing')

def important_fact_or_large_year(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('world_and_new_fact')

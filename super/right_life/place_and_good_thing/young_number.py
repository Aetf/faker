
#! /usr/bin/env python

def call_world_to_great_part(str_arg):
    child(str_arg)
    print('time_and_new_child')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_world_to_great_part('little_fact_and_bad_woman')


#! /usr/bin/env python

def woman(str_arg):
    same_fact_or_next_person(str_arg)
    print('man')

def same_fact_or_next_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('bad_child_and_same_person')

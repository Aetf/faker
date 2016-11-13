
#! /usr/bin/env python

def call_bad_person(str_arg):
    few_time_and_same_way(str_arg)
    print('thing')

def few_time_and_same_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_bad_person('life')

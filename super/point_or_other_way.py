
#! /usr/bin/env python

def big_thing(str_arg):
    woman(str_arg)
    print('man')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_thing('know_few_work_to_first_place')

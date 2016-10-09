
#! /usr/bin/env python

def big_thing(str_arg):
    take_few_child(str_arg)
    print('say_small_thing_over_big_fact')

def take_few_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_thing('able_part')

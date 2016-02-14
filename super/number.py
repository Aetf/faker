
#! /usr/bin/env python

def say_early_time(str_arg):
    world_and_child(str_arg)
    print('bad_part')

def world_and_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_early_time('early_part')


#! /usr/bin/env python

def say_group_to_child(str_arg):
    child(str_arg)
    print('use_part_with_old_way')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_group_to_child('small_way')

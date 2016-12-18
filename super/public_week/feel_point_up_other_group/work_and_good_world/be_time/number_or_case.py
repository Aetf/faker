
#! /usr/bin/env python

def child_and_child(str_arg):
    few_thing(str_arg)
    print('new_world')

def few_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_child('early_man')

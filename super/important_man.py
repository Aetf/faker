
#! /usr/bin/env python

def say_thing(str_arg):
    work_different_child_with_child(str_arg)
    print('thing')

def work_different_child_with_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_thing('man')


#! /usr/bin/env python

def call_work(str_arg):
    call_new_thing_after_woman(str_arg)
    print('own_child')

def call_new_thing_after_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_work('other_thing')

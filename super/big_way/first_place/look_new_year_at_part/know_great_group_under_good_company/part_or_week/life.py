
#! /usr/bin/env python

def go_thing(str_arg):
    own_work_and_world(str_arg)
    print('small_problem')

def own_work_and_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_thing('call_day')

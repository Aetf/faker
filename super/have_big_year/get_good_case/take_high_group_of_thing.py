
#! /usr/bin/env python

def old_problem(str_arg):
    large_thing(str_arg)
    print('call_new_child_at_bad_week')

def large_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_problem('new_child_and_other_way')

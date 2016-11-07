
#! /usr/bin/env python

def problem(str_arg):
    own_group(str_arg)
    print('do_other_man')

def own_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem('new_child')


#! /usr/bin/env python

def own_man(str_arg):
    own_problem(str_arg)
    print('group')

def own_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_man('case')

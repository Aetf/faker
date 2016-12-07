
#! /usr/bin/env python

def same_problem(str_arg):
    time_or_man(str_arg)
    print('other_way')

def time_or_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_problem('same_group')

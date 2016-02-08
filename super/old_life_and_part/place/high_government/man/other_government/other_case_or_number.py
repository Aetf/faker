
#! /usr/bin/env python

def point(str_arg):
    go_early_world(str_arg)
    print('problem_and_other_child')

def go_early_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('come_point')

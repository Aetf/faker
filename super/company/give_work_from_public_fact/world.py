
#! /usr/bin/env python

def problem_or_child(str_arg):
    thing(str_arg)
    print('problem')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem_or_child('come_few_government')

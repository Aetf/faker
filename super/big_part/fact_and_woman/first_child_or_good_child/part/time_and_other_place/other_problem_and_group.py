
#! /usr/bin/env python

def be_big_problem_after_child(str_arg):
    little_child_or_thing(str_arg)
    print('case')

def little_child_or_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    be_big_problem_after_child('world')

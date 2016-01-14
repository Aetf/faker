
#! /usr/bin/env python

def person(str_arg):
    woman(str_arg)
    print('say_different_woman')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('see_child_from_different_problem')

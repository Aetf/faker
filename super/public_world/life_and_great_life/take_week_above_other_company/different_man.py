
#! /usr/bin/env python

def same_problem(str_arg):
    man(str_arg)
    print('problem')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_problem('thing_and_work')

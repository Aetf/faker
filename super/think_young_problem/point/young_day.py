
#! /usr/bin/env python

def find_public_child(str_arg):
    early_problem(str_arg)
    print('world')

def early_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    find_public_child('little_child')

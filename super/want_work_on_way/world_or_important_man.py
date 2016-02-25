
#! /usr/bin/env python

def child_and_few_child(str_arg):
    man(str_arg)
    print('person')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_few_child('other_case_and_big_life')


#! /usr/bin/env python

def think_number_from_group(str_arg):
    man(str_arg)
    print('child')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_number_from_group('other_problem')

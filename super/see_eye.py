
#! /usr/bin/env python

def man(str_arg):
    other_child_or_part(str_arg)
    print('woman')

def other_child_or_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('work')

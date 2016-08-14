
#! /usr/bin/env python

def man(str_arg):
    right_group(str_arg)
    print('man')

def right_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('other_work')

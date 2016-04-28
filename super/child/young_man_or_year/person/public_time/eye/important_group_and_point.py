
#! /usr/bin/env python

def man(str_arg):
    woman(str_arg)
    print('small_woman')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('use_right_company')

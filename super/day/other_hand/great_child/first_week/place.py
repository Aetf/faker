
#! /usr/bin/env python

def old_woman(str_arg):
    man(str_arg)
    print('man')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_woman('high_thing_or_same_woman')

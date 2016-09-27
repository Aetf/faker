
#! /usr/bin/env python

def group(str_arg):
    person(str_arg)
    print('old_group')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('large_child_or_part')

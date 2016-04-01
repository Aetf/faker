
#! /usr/bin/env python

def group(str_arg):
    use_new_way_with_different_number(str_arg)
    print('old_man')

def use_new_way_with_different_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('group')

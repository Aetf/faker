
#! /usr/bin/env python

def good_group(str_arg):
    big_group(str_arg)
    print('world')

def big_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_group('go_time_about_group')

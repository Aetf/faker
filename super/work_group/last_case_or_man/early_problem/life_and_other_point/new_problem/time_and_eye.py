
#! /usr/bin/env python

def feel_bad_way(str_arg):
    man_or_child(str_arg)
    print('old_man')

def man_or_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    feel_bad_way('long_point')

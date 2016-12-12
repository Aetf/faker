
#! /usr/bin/env python

def bad_point(str_arg):
    say_child_about_same_time(str_arg)
    print('child')

def say_child_about_same_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_point('other_world')

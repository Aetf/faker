
#! /usr/bin/env python

def good_child(str_arg):
    person(str_arg)
    print('problem_or_bad_child')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_child('old_point')

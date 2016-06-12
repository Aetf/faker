
#! /usr/bin/env python

def see_bad_person(str_arg):
    have_person(str_arg)
    print('group')

def have_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_bad_person('thing_or_different_woman')

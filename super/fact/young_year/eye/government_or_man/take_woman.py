
#! /usr/bin/env python

def large_person(str_arg):
    small_woman(str_arg)
    print('world')

def small_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_person('life_and_place')

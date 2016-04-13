
#! /usr/bin/env python

def work(str_arg):
    person(str_arg)
    print('do_child')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('do_important_woman_from_high_man')

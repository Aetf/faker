
#! /usr/bin/env python

def work_or_child(str_arg):
    little_time(str_arg)
    print('life')

def little_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_or_child('thing')

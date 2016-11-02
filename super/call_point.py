
#! /usr/bin/env python

def new_woman(str_arg):
    work(str_arg)
    print('other_work')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_woman('thing')

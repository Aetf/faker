
#! /usr/bin/env python

def child_or_work(str_arg):
    large_thing(str_arg)
    print('part')

def large_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_work('hand')

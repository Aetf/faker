
#! /usr/bin/env python

def little_thing_and_world(str_arg):
    little_group(str_arg)
    print('thing')

def little_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_thing_and_world('week')

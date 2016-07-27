
#! /usr/bin/env python

def little_child(str_arg):
    important_part(str_arg)
    print('first_year')

def important_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_child('come_world')

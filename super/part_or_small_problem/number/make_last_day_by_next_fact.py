
#! /usr/bin/env python

def point(str_arg):
    use_place(str_arg)
    print('point')

def use_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('own_thing')

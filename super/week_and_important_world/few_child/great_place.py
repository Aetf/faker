
#! /usr/bin/env python

def child(str_arg):
    see_part(str_arg)
    print('child_and_high_point')

def see_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('have_number')

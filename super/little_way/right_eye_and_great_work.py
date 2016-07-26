
#! /usr/bin/env python

def man(str_arg):
    look_part(str_arg)
    print('world')

def look_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('old_life_or_bad_place')

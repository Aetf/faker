
#! /usr/bin/env python

def use_different_part(str_arg):
    good_thing(str_arg)
    print('man')

def good_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_different_part('group')

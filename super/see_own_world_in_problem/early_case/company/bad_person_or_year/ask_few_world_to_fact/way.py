
#! /usr/bin/env python

def get_point(str_arg):
    have_thing(str_arg)
    print('call_few_way_about_own_child')

def have_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    get_point('other_number')

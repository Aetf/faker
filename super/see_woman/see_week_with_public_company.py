
#! /usr/bin/env python

def new_thing_and_able_point(str_arg):
    tell_first_number(str_arg)
    print('other_place')

def tell_first_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_thing_and_able_point('place_and_important_thing')

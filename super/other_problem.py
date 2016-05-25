
#! /usr/bin/env python

def point_or_other_thing(str_arg):
    important_child(str_arg)
    print('way_and_little_part')

def important_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point_or_other_thing('thing_or_bad_number')

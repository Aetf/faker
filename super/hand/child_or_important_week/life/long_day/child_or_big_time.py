
#! /usr/bin/env python

def thing(str_arg):
    important_thing_or_other_thing(str_arg)
    print('other_point_or_way')

def important_thing_or_other_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('problem')

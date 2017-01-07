
#! /usr/bin/env python

def eye_or_other_thing(str_arg):
    little_world(str_arg)
    print('own_way')

def little_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye_or_other_thing('big_person')

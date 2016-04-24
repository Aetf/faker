
#! /usr/bin/env python

def have_thing(str_arg):
    different_part(str_arg)
    print('make_work')

def different_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    have_thing('leave_able_way')


#! /usr/bin/env python

def case(str_arg):
    early_thing(str_arg)
    print('thing_and_group')

def early_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('bad_thing')

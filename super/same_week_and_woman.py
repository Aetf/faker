
#! /usr/bin/env python

def early_place(str_arg):
    other_thing(str_arg)
    print('old_man')

def other_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_place('person')

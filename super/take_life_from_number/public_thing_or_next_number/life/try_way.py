
#! /usr/bin/env python

def go_world(str_arg):
    first_person_and_early_thing(str_arg)
    print('early_part')

def first_person_and_early_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_world('work')

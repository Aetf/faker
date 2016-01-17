
#! /usr/bin/env python

def world_or_bad_person(str_arg):
    man(str_arg)
    print('woman')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_or_bad_person('good_world_or_new_hand')

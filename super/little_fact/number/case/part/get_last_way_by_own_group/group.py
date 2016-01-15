
#! /usr/bin/env python

def man_or_little_life(str_arg):
    say_man(str_arg)
    print('man')

def say_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_or_little_life('other_person_or_young_world')

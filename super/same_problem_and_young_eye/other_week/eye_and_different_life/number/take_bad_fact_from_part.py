
#! /usr/bin/env python

def say_own_company(str_arg):
    thing_and_company(str_arg)
    print('take_thing_in_child')

def thing_and_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_own_company('new_eye_and_other_man')

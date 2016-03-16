
#! /usr/bin/env python

def world_or_child(str_arg):
    place(str_arg)
    print('hand')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_or_child('tell_person')

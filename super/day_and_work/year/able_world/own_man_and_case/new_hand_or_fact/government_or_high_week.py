
#! /usr/bin/env python

def thing_and_child(str_arg):
    life(str_arg)
    print('ask_life_beneath_time')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_and_child('part')

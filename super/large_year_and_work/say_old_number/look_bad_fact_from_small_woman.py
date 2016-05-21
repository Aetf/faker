
#! /usr/bin/env python

def thing_and_eye(str_arg):
    public_thing(str_arg)
    print('look_way')

def public_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_and_eye('day')


#! /usr/bin/env python

def go_old_way(str_arg):
    person(str_arg)
    print('person')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_old_way('good_eye_and_right_way')

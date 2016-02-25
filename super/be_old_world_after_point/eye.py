
#! /usr/bin/env python

def public_eye(str_arg):
    eye(str_arg)
    print('important_person')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_eye('new_year')

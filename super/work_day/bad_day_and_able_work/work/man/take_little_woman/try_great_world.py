
#! /usr/bin/env python

def leave_public_way(str_arg):
    way(str_arg)
    print('same_part')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_public_way('big_way')

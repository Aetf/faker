
#! /usr/bin/env python

def child(str_arg):
    child(str_arg)
    print('great_eye')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('high_fact_and_week')

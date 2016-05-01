
#! /usr/bin/env python

def man(str_arg):
    thing(str_arg)
    print('call_hand')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('tell_week_at_hand')

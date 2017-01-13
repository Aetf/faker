#! /usr/bin/env python

import datetime
import random

DT_FMT = '%Y-%m-%d %H:%M:%S'
ZERO_FRQ = 10
DSS = 60 * 60 * 24


def second_list(s, n):
    sl = []
    for i in range(n):
        sl.append(random.randint(0, s))
    return sorted(sl)


def rand_frq(frq):
    frq_l = []
    for i in range(1, frq + 1):
        frq_l += [i]*(frq+1-i)
        frq_l.append(i)
    frq_l = frq_l * ZERO_FRQ + [0] * len(frq_l)
    return lambda: random.choice(frq_l)


def dt_list(dt, sl):
    return [dt + datetime.timedelta(seconds=s) for s in sl]


def dt2str(dt):
    return dt.strftime(DT_FMT)


def str2dt(dt):
    return datetime.datetime.strptime(dt, DT_FMT)


def str_dt_list(dt, sl):
    return [dt2str(ddtt) for ddtt in dt_list(dt, sl)]


def std_sdl(dtf, n, rf):
    sdl = []
    for i in range(n):
        dt = dtf + datetime.timedelta(days=i)
        sl = second_list(DSS, rf())
        sdl += str_dt_list(dt, sl)
    return sdl


def dt_pick(dt_from, dt_to, frq):
    dtf = str2dt(dt_from)
    dtt = str2dt(dt_to)
    delta = dtt - dtf

    if delta.days < 0:
        return []

    #rf = rand_frq(frq)
    rf = lambda: frq

    dl = []

    if delta.days == 0:
        sl = second_list(delta.seconds, rf())
        dl += str_dt_list(dtf, sl)
        return dl

    a_dtf = datetime.datetime(dtf.year, dtf.month, dtf.day) + datetime.timedelta(days=1)
    b_dtt = datetime.datetime(dtt.year, dtt.month, dtt.day)

    slf = second_list((a_dtf - dtf).seconds, rf())
    dl += str_dt_list(dtf, slf)

    dl += std_sdl(a_dtf, (b_dtt - a_dtf).days, rf)

    slt = second_list((dtt - b_dtt).seconds, rf())
    dl += str_dt_list(b_dtt, slt)

    return dl


if __name__ == '__main__':
    print(dt_pick('2013-12-14 12:23:34', '2013-12-18 4:23:12', 5))

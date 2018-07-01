# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input

    output = output.replace(u'\u106A', u'\u1009')
    #  nya lay

    output = output.replace(u'\u106B', u'\u100A')
    #  nya

    output = output.replace(u'\u103B', u'\u103C')
    output = output.replace(u'\u107E', u'\u103C')
    output = output.replace(u'\u107F', u'\u103C')
    output = output.replace(u'\u1080', u'\u103C')
    output = output.replace(u'\u1081', u'\u103C')
    output = output.replace(u'\u1082', u'\u103C')
    output = output.replace(u'\u1083', u'\u103C')
    output = output.replace(u'\u1084', u'\u103C')
    # yayit

    output = output.replace(u'\u1033', u'\u102F')
    # 1chaung

    output = output.replace(u'\u1034', u'\u1030')
    #2chaung

    output = output.replace(u'\u103D', u'\u103E')
    output = output.replace(u'\u107D', u'\u103E')
    output = output.replace(u'\u1087', u'\u103E')
    #hahtoe

    output = output.replace(u'\u1090', u'\u101B')
    #yacout

    output = output.replace(u'\u1092', u'\u100C')
    #htaonepae

    output = output.replace(u'\u106E', u'\u100D')
    #dayinkout

    output = output.replace(u'\u1097', u'\u100B')
    #tatalin

    output = output.replace(u'\u108F', u'\u1014')
    #nange

    output = output.replace(u'\u103A', u'\u103B')
    #yapin

    output = output.replace(u'\u1039', u'\u103A')
    #athat

    output = output.replace(u'\1086', u'\u103F')
    #thagyi



    return output



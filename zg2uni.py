# -*- coding: utf-8 -*-
import re
def re_sub(pattern, replacement, string):
    def _r(m):
        class _m():
            def __init__(self, m):
                self.m=m
                self.string=m.string
            def group(self, n):
                return m.group(n) or ""
        return re._expand(pattern, _m(n), replacement)

    return re.sub(pattern, _r, string)


def convert(input):
    tallAA = u'\u102B'
    aa = u'\u102C'
    vi = u'\u102D'

    #lone gyi tin
    ll = u'\u102E'
    u = u'\u102F'
    uu = u'\u1030'
    ve = u'\u1031'
    ai = u'\u1032'
    ans = u'\u1036'
    db = u'\u1037'
    visarge = u'\u1038'

    asat = u'\u103A'

    ya = u'\u103B'
    ra = u'\u103C'
    wa = u'\u103D'
    ha = u'\u103E'
    zero = u'\u1040'
    output = input

    output = output.replace(u'\u106A', u'\u1009')
    #  nya lay

    output = output.replace(u'\u106B', u'\u100A')
    #  nya

    output = re.sub(u'[\u103D\u1087]', u'\u103E', output)
    #hahtoe

    output = output.replace(u'\u103C', u'\u103D')
    #wa swae

    output = output.replace(u'\u103B', u'\u103C')
    output = output.replace(u'\u107E', u'\u103C')
    output = output.replace(u'\u107F', u'\u103C')
    output = output.replace(u'\u1080', u'\u103C')
    output = output.replace(u'\u1081', u'\u103C')
    output = output.replace(u'\u1082', u'\u103C')
    output = output.replace(u'\u1083', u'\u103C')
    output = output.replace(u'\u1084', u'\u103C')
    # yayit

    output = output.replace(u'\u103A', u'\u103B')
    output = output.replace(u'\u107D', u'\u103B')
    #yapin

    output = output.replace(u'\u1039', u'\u103A')
    # athat

    output = output.replace(u'\u1090', u'\u101B')
    #yacout

    output = output.replace(u'\u108F', u'\u1014')
    # nange

    output = output.replace(u'\u1097', u'\u100B')
    #tatalin

    output = output.replace(u'\u1033', u'\u102F')
    # 1chaung

    output = output.replace(u'\u1034', u'\u1030')
    #2chaung

    output = output.replace(u'\u1092', u'\u100C')
    #htaonepae

    output = output.replace(u'\u106E', u'\u100D')
    #dayinkout

    output = output.replace(u'\u1086', u'\u103F')
    #thagyi

    output = re.sub(u'\u1060', u'\u1039\u1000', output) #ka_gyi
    output = re.sub(u'\u1061', u'\u1039\u1001', output) #ka_kwae
    output = re.sub(u'\u1062', u'\u1039\u1002', output) #ga_nge
    output = re.sub(u'\u1063', u'\u1039\u1003', output) #ga_hagyi
    output = re.sub(u'\u1065', u'\u1039\u1005', output) #sa_lone
    output = re.sub(u'[\u1066\u1067]', u'\u1039\u1006', output) #sa_lane
    output = re.sub(u'\u1068', u'\u1039\u1007', output) #za_kwae
    output = re.sub(u'\u1069', u'\u1039\u1009', output) #za_myin_zwae
    output = re.sub(u'\u1070', u'\u1039\u100F', output) #na_gyi
    output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010', output) #ta_win_pu
    output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011', output)#hta_sin_tu
    output = re.sub(u'\u1075', u'\u1039\u1012', output) #da_dway
    output = re.sub(u'\u1076', u'\u1039\u1013', output) #da_oak
    output = re.sub(u'\u1077', u'\u1039\u1014', output) #na_nge
    output = re.sub(u'\u1078', u'\u1039\u1015', output) #pa_saut
    output = re.sub(u'\u1079', u'\u1039\u1016', output) #pha_oo_hoat
    output = re.sub(u'\u107A', u'\u1039\u1017', output) #ba_dad
    output = re.sub(u'[\u107B\u1093]', u'\u1039\u1018', output) #ba_kone
    output = re.sub(u'\u107C', u'\u1039\u1019', output) #ma
    output = re.sub(u'\u1085', u'\u1039\u101C', output) #hla
    #passin

    output = re.sub(u'\u105A', u'\u102B' + u'\u103A', output) # yaechar_shaehtoe

    output = re.sub(u'\u108A', u'\u103D' + u'\u103E', output) #wa_hatoe

    output = re.sub(u'\u1088', u'\u103E' + u'\u103F', output) #hatoe_tachaunge

    output = re.sub(u'\u1089', u'\u103E' + u'\u1030', output) #hatoe_nachaunge

    output = re.sub(u'\u103E\u103B', u'\u103B' + u'\u103E', output) #ypin_hatoe

    output = re.sub(u'\u108B', u'\u102D' + u'\u1004' + u'\u1039' + u'\u103A', output) #ngathat_lgt

    output = re.sub(u'\u108C', u'\u1004' + u'\u100A' + u'\u1039' + u'\u102E', output) #ngathat_lgt_sankhat

    output = re.sub(u'\u108D', u'\u1004' + u'\u103A' + u'\u1039' + u'\u1036', output) #ngathat_tttin

    output = re.sub(u'\u108E', u'\u102D' + u'\u1036', output)  # lonegt_tttin

    output = re.sub(u'\u1064', u'\u1004\u103A\u1039', output) # up_ngathat

    output = re.sub(u'u\u104E', u'\u104E\u1004\u103A\u1038', output) #ll_kaung

    ##pattern

    output = re.sub(u'(\u103C)([\u1000-\u1021])(\u1039[\u1000-\u1021])?', r'\2\3\1', output) #yayit

    output = re.sub(u'([\u103B\u103C])(\u103D)(\u103E)', r'\1\2\3', output) #pin_yit_swae_htoe

    output = re.sub(u'([\u103B\u103C])(\u103E)', r'\1\2', output) #pin_yit_htoe

    output = re.sub(u'([\u103B\u103C])(\u103D)', r"\\1\\2", output) #pin_yit_swae

    output = re.sub(u'(\u1030)([\u1000-\u1021])(\u103B\u103C\u103D\u103E\u102B\u102C\u1037\u1038)', r'\1\2\3', output) #thwayhtoe

    output = re.sub(u'[\u1094\u1095]', u'\u1037', output) #outkamyint


    return output


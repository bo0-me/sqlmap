#!/usr/bin/env python
#
#  Script for getting Yandex tIC of page
#
#  Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

import urllib
import xml.etree.ElementTree as ET
import json

def get_tic(url):
    _ = 'http://bar-navig.yandex.ru/u'
    params = urllib.urlencode({
        'ver':2,
        'show':1,
        'url': _
    })

    # try:
    r = urllib.urlopen(_, data=params)

    if r.code == 200:
        tree = ET.fromstring(r.read()).find('tcy')
        rank = tree.attrib['rang']
    else:
        rank = 'Err'
    return rank
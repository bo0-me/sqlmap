#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Script for getting Yandex tIC of page
#
#  Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

import urllib
import xml.etree.ElementTree as ET

def get_tic(url):
    _ = 'http://bar-navig.yandex.ru/u?%s'
    params = {
        'ver':2,
        'show':1,
        'url': url,
    }

    link = _ % urllib.urlencode(params.items())

    r = urllib.urlopen(link)

    if r.code == 200:
        tree = ET.fromstring(r.read()).find('tcy')
        rank = int(tree.attrib['rang'])
    else:
        rank = 'Err'
    return rank
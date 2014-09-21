#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Script for getting Yandex tIC of page
#
#  Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

import urllib
import xml.etree.ElementTree as ET


def get_tic(url):
    _ = 'http://bar-navig.yandex.ru/u?ver=2&show=1&url=%s'

    r = urllib.urlopen(_ % urllib.unquote(url).encode("ascii"))
    try:
        if r.code == 200:
            tree = ET.fromstring(r.read()).find('tcy')
            rank = int(tree.attrib['rang'])
    except Exception:
        rank = 0

    return rank
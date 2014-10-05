#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Checks where is administrator hole for this URL
#
#  Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

import re

import grequests

from lib.core.common import clearConsoleLine
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.enums import WEB_API
from urlparse import urlsplit


def concateurl(url):
    l = []
    walist = [wa for wa in dir(WEB_API) if not wa.startswith('__')]
    for _ in kb.commonAdmin:
        if re.search(r'XXXX', _):
            l.extend([''.join([url, re.sub("XXXX", wa, _)]) for wa in walist])
        else:
           l.append(''.join([url, _]))
    return l


def searchadminpanel(url):
    try:
        infomsg = "starting search admin page"
        if conf.bulkFile:
            infomsg += " for URLs %r" % url
        logger.info(infomsg)

        urlbase = re.match(r'(.+)[/]+', url).group(0)
        target = concateurl(urlbase)
        target += concateurl('http://%s/' % urlsplit(url).netloc)
        target = set(target)
        foundAdminPanel = False
        rs = (grequests.get(u) for u in target)
        for r in grequests.map(rs):
            if r.status_code == 200:
                warnmsg = "Possible admin control panel for target URL: "
                warnmsg += "'%s'" % url
                warnmsg += " is %s" % r.url
                logger.warn(warnmsg)
                foundAdminPanel = True

        if not foundAdminPanel:
            warnmsg = "Admin control panel not found for target URL: "
            warnmsg += "'%s'" % url
            logger.warn(warnmsg)

    except KeyboardInterrupt:
        warnmsg = "user aborted during admin page searching. sqlmap "
        warnmsg += "will try to continue"
        logger.warn(warnmsg)

    finally:
        clearConsoleLine(True)

#
# if conf.verbose in (1, 2):
#     status = "%d/%d links checked (%d%%)" % (i + 1, len(targets), round(100.0 * (i + 1) / len(targets)))
#     dataToStdout("\r[%s] [INFO] %s" % (time.strftime("%X"), status), True)
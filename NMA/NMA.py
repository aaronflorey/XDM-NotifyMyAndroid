# Author: Dennis Lutter <lad1337@gmail.com>
# URL: https://github.com/lad1337/XDM
#
# This file is part of XDM: eXtentable Download Manager.
#
#XDM: eXtentable Download Manager. Plugin based media collection manager.
#Copyright (C) 2013  Dennis Lutter
#
#XDM is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#XDM is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see http://www.gnu.org/licenses/.

from xdm.plugins import *
from libs.pyname import pynma

class NMA(Notifier):
    version = "0.1"
    identifier = "me.mochaka.nma"
    addMediaTypeOptions = False
    _config = {'nma_apikey': ''}
    config_meta = {'nma_apikey': {'human': 'NotifyMyAndroid API Key',
                                    'desc': 'The API Key from your NotifyMyAndroid account, for sending notifications to android.'}}

    def sendMessage(msg, element=None):
        
        if not self.c.nma_apikey:
            log.error("NMA API Key not set.")
            return False

        p = PyNMA(self.c.nma_apikey)

        r = p.push('XDM', 'XDM Notification', msg)

        if(r.code == 200):
            log("NMA code %s" % r.code)
            return True
        else:
            log('NMA Error: %s, %s', % (r.code, r.message))
            return False
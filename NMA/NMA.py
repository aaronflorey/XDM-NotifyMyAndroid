# Author: Aaron Florey
# URL: https://raw.github.com/Mochaka/XDM-NotifyMyAndroid
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
from libs import pynma
from pprint import pprint

class NMA(Notifier):
    identifier = "me.mochaka.nma"
    version = "0.1"
    addMediaTypeOptions = False
    _config = {'nma_apikey': ''}

    def sendMessage(self, msg, element=None):
        
        if not self.c.nma_apikey:
            log.error("NMA API Key not set.")
            return False

        return self._sendMessage(msg)

    def _sendMessage(self, msg):
        apikey = str(self.c.nma_apikey)

        if not self.c.nma_apikey:
            log.error("NMA API Key not set.")
            return False

        p = pynma.PyNMA(apikey)

        r = p.push('XDM', 'XDM Notification', msg)

        if(str(r[apikey]['code']) == '200'):
            log("NMA code %s" % r[apikey]['code'])
            return True
        else:
            log('NMA Error: %s, %s' % (r[apikey]['code'], r[apikey]['message']))
            return False

    def _sendTest(self, nma_apikey):
        result = self._sendMessage('Test From XDM')
        if result:
            return (result, {}, 'Message sent. Check your device(s)')
        else:
            return (result, {}, 'Message NOT sent. Check your API Key')
    _sendTest.args = ['nma_apikey']

    config_meta = {'nma_apikey': {'human': 'NotifyMyAndroid API Key',
                                    'desc': 'The API Key from your NotifyMyAndroid account, for sending notifications to android.'},
                    'plugin_buttons': {'sendTest': {'action': _sendTest, 'name': 'Send test'}}}
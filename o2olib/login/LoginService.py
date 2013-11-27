# -*- coding: utf-8 -*-

'''
Created on 2013年11月15日

@author: liufang.deng
'''

from o2olib import GuestService
from datetime import datetime

class LoginService(object):
    
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls != type(cls.__instance):
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance
    
    def login(self,args):
        guest = self.build_guest(args)
        guests = GuestService.gets(guest)
        if len(guests) == 0:
            guest = self.get_guest(args)
            guest["register_date"] = datetime.now()
            guest["last_active_date"] = datetime.now()
            guest["id"] = GuestService.add(guest)
        else:
            guest = guests[0]
            guest["last_active_date"] = datetime.now()
            GuestService.update(guest)
        return guest
    
    def build_guest(self,args):
        pass
    
    def get_guest(self,args):
        pass

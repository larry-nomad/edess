import json

class JsonResult:
    ret = None
    msg = None
    data = None

    def __init__(self,data = None):
        self.data = data
        self.ret = u"success"        

    def set_error_msg(self, msg):
        self.msg = msg
        self.ret = u"fail"
        return self

    def to_dic(self):
        d = {}
        d.update(self.__dict__)
        return d



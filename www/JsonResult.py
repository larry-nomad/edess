class JsonResult:
    ret = None
    msg = None
    data = None

    def __init__(self,data = None):
        self.data = data
        self.ret = u"success"

    def setErrorMsg(self, msg):
        self.msg = msg
        self.ret = u"fail"

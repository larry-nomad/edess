class QException(Exception):
    code = 800

    def __init__(self, msg, code = None, payload = None):
        Exception.__init__(self)
        self.message = msg
        if code is not None:
            self.code = code
        self.payload = payload

    def to_dic(self):
        rs = {}
        rs["status"] = self.code
        rs['message'] = self.message
        return rs

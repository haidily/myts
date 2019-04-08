# coding = utf-8

#常量类
class MyConst:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if self.__dict__.__contains__(name):
            raise self.ConstError("cannot change const.%s" % name)
        if not name.isupper():
            raise self.ConstCaseError("const name '%s' is not all upper" % name)
        self.__dict__[name] = value
class DataflowFunctionCall:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def execute(self):
        args = [arg.execute() if isinstance(arg, type(self)) else arg for arg in self.args]
        return self.func(*args)

class DataflowFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return DataflowFunctionCall(self.func, *args)

def dataflow(func):
    return DataflowFunction(func)

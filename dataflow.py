def _resolve(arg, assignments={}):
    if isinstance(arg, DelayedFunctionCall):
        return arg.execute(assignments)
    elif isinstance(arg, Variable):
        return assignments[arg]
    return arg

class DelayedFunctionCall:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def execute(self, assigments={}):
        # step 1: resolve input paramaters
        args = [_resolve(arg, assigments) for arg in self.args]
        kwargs = {k: _resolve(v, assigments) for k, v in self.kwargs.items()}

        # step 2: compute function call given input parameters
        return self.func(*args, **kwargs)

def dataflow(func):
    # "calling" the function will instead bind the input parameters
    return lambda *args, **kwargs: DelayedFunctionCall(func, *args, **kwargs)

class Variable:
    pass

from dataflow import dataflow

@dataflow
def f(g, seed):
    return g**2 % seed

@dataflow
def g(a, b, h):
    return a * b + h

@dataflow
def h(c, d):
    return c / d

seed = 5

# ---

# setting up the execution / dataflow
graph = f(g(1, 2, h(3, 4)), seed)
# no addition or multiplication has happened yet

# executing the dataflow
print(graph.execute())

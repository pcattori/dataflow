from dataflow import dataflow, Variable

@dataflow
def f(x, y):
    return x**2 % y

@dataflow
def g(a, b, c):
    return a * b + c

@dataflow
def h(i, j):
    return i / j

z = Variable()
seed = Variable()

# setting up the execution / dataflow
graph = f(g(z, 2, h(4, z)), seed)
# no addition or multiplication has happened yet

# executing the dataflow
print(graph.execute({z: 1., seed: 5}))
print(graph.execute({z: 3., seed: 13}))

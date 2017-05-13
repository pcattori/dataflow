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
seed = df.Variable()

# setting up the dataflow graph
graph = f(g(z, 2, h(4, z)), seed)
# bodies of f,g,h functions have not executed yet

# executing the dataflow graph
print(graph.execute({z: 1., seed: 5}))
print(graph.execute({z: 3., seed: 13}))

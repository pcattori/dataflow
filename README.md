# usage

```python
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

# setting up the execution / dataflow
graph = f(g(1, 2, h(3, 4)), seed)

# no addition or multiplication has happened yet

# executing the dataflow
print(graph.execute())
```

Note the use of the `@dataflow` decorator. If you want you could also define the functions regularly and later convert them into `DataflowFunctions`:

```python
def f(g, seed):
    return g**2 % seed

# do stuff with regular, non-dataflow f

f = dataflow(f) # now f is a DataflowFunction
```

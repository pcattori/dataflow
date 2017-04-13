# dataflow

Toy example of setting up a delayed-execution graph, or ["dataflow"](https://www.tensorflow.org/versions/r0.11/resources/faq) in [TensorFlow](https://www.tensorflow.org/) terminology.

Check out the [stackoverflow question that inspired this demo](http://stackoverflow.com/a/43380155/1490091).

# usage

## step 1
Use the `@dataflow` decorator to wrap a function with dataflow capabilities:

```python
@dataflow
def f(x, y):
    return x**2 % y

@dataflow
def g(a, b, c):
    return a * b + c

@dataflow
def h(i, j):
    return i / j
```

Calling these function will now store the function and arguments for execution at a later point.

In other words, no mathematical operations will happen until you call
`graph.execute()` in step 3.

## step 2
Compose many `@dataflow` functions into a graph:

```python
graph = f(g(1, 2, h(3, 4)), 5)
```

## step 3
Execute the function:

```python
answer = graph.execute()
```

## variables

You can also define variables that get bound to values at execution time:

```python
z = Variable()
seed = Variable()

graph = f(g(z, 2, h(4, z)), seed)
```

You can execute the same graph with different values bound to the variables:

```python
answer1 = graph.execute({z: 1., seed: 5})
answer2 = graph.execute({z: 3., seed: 13})
```

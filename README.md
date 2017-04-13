# dataflow

Toy example of setting up a delayed-execution graph, or ["dataflow"](https://www.tensorflow.org/versions/r0.11/resources/faq) in [TensorFlow](https://www.tensorflow.org/) terminology.

Check out the [stackoverflow question that inspired this demo](http://stackoverflow.com/a/43380155/1490091).

# usage

Use the `@dataflow` decorator to wrap a function with dataflow capabilities:

```python
@dataflow
def f(x, y):
    return x**2 % y
```

Compose many `@dataflow` functions into a graph:

```python
graph = f(g(1, 2, h(3, 4)), 5)
```

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


# Functions lab

As we know, we can use functions to give a name to sequences of our code, to make it more expressive.  We can also use functions to allow us to reuse code.  In this lab we will get practice in using functions for these purposes.

### Objectives

* Practice declaring and returning values from function
* Practice accessing variables outside of a function's scope, from inside of a function

### Writing our first functions

Imagine we work in a diner.  We have a list of `orders` which we assign below.  Write a function called `number_of_orders` that returns the current number of orders.


```python
orders = ['turkey sandwich', 'eggs']
def number_of_orders():
    pass
```


```python
number_of_orders() # 2
```

Now write another function called `next_up` that returns the first order (the order with the lowest index), in the `orders` list.


```python
def next_up():
    pass
```


```python
orders = ['turkey sandwich', 'eggs']
next_up() # 'turkey sandwich'

orders = ['beet salad', 'fennel']
next_up() # 'beet salad'
```

Ok, now write a function called `healthy_order` that returns the string `'spinach salad'`.


```python
def healthy_order():
    pass
```


```python
healthy_order() # 'spinach salad'
```

Now let's declare an array called `orders`.  Change the function `healthy_order` so that it continues to return the string `'spinach salad'`, but also adds the string `'spinach salad'` to the end of the list of orders.


```python
orders = ['turkey sandwich', 'eggs']
healthy_order()
orders[-1] # 'spinach salad'
```




    'eggs'



Now let's write another function iterates through the list of `orders` and capitalizes the first letter of each word in the order.  It should return a list of capitalized orders.


```python
orders = ['spinach salad', 'turkey sandwich']
def capitalize_orders():
    pass
```


```python
capitalize_orders() # ['Spinach Salad', 'Turkey Sandwich']
```

Now if someone adds, an upcapitalized order, we can simply call our function again to return a list of capitalized orders.


```python
orders = ['spinach salad', 'turkey sandwich']
capitalize_orders() # ['Spinach Salad', 'Turkey Sandwich']
orders.append('eggs')
capitalize_orders() # ['Spinach Salad', 'Turkey Sandwich', 'Eggs']
```

### Summary

Great job.  Through this lab you were able to get practice both writing and returning values from functions.  You also practiced accessing variables not local to the function, but in the global scope.

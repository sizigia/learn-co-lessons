
# Being expressive with functions

### Learning objectives

* Understand what it means to say that a function is dependent on a variable
* Understand how to express a multivariable function 
* Understand how to express a function that is composed of another function, and why we express functions that way  

### Introduction

Concepts in mathematics and in code tend to align.  Both are mechanisms to express an idea and model the world around it.  It's time we go off on a little bit of a tangent to explore how denoting functions in math aligns with denoting functions in code.  Some of these concepts may feel like review, but solidifying this foundation will provide clarity when we move on to explore other mathematical topics.

### Expressing functions

Let's find a way to talk about functions in general.  We describe a function as $f(x)$.  $f(x)$ is our generic way to express a function.  We are not saying the output equals $y$ or anything else, we are just saying that the function returns an output.  For example, we can say the following:

$$f(x) = 3x$$

The expression above means that there is an output that equals 3 times $x$.  

Note this *mathematical* expression of an output varying with an input lines up nicely with expressing *programmatically* how a function varies with an input.  In programming, we simply can use an argument to show that a function varies with an input.


```python
def f(x):
    return 3*x
```


```python
f(3)
```




    9



### Evaluating functions at specific values

Let's evaluate the function $f(x)$ at specific values of $x$.  So when $x = 3$, $f(x) = 3x = 3*3 = 9$.  And when $x = 4$,  $f(x) = 4*3 = 12$.  Another way of saying "when $x = 3$ is simply to say $f(3)$.  So:
$$f(3) = 9$$

$$f(4) = 12$$

That looks pretty similar to how we would evaluate a function at a specific value in code.


```python
f(3)
```




    9




```python
f(4)
```




    12



So far it feels like a small leap to go from expressing a function in math to expressing a function in code.

### Unpacking  the $x$ in  $f(x)$

So the $x$ part of $f(x)$ indicates that the function produces different outputs with different values of $x$.  As our values of $x$ change, the output of the function also changes.  By describing our function as $f(x)$, or as "a function of $x$", we also indicate that the same $x$ input always returns the same output from the function.  

Now take a look at another function:

$$ f = 3x + y$$

To determine this output, we need to know more than a specific value of $x$.  We also need to know the value of $y$.  So it's no longer the case that a specific input of $x$ always returns the same output from this function.  After all, if we fill in that x = 4, then $f = 3*4 + y$, and $f$ would still vary with different $y$ values. 

It is not just a specific input of $x$ that returns the same input, but specific inputs of $x$ *and $y$* that always return the same output.  We indicate this like so:

$$ f(x,y) = 3x + y$$


```python
def f(x,y):
    return 3*x + y
```

And to indicate that we are evaluating the function at specific values of $x$ and $y$, we write the following: 

$$ f(3,4) = 3*3 + 4 = 13$$


```python
f(3, 4)
```




    13



A function whose output depends on *multiple* variables, like $x$ and $y$, is called a **multivariable function**.

#### Test your knowledge

Take a look at a new function.  How would we express the function:

$$ f = 3x + 4$$

Is that a multi-variable function?  Well, while the number 4 influences the output of the function, we do not need to know anything but the value of $x$ in order to determine the output of the function.  So we still would express that function as a single variable function:

$$ f(x) = 3x + 4$$

And in code:


```python
def f(x):
    return 3*x + 4
```

### Unpacking  the $f$ in  $f(x)$

Now that we understand the significance of $x$ in $f(x)$ what does the $f$ mean?  Well not too much.  It just a label for a specific function.  We could easily written our previous function as:

$$ g(x) = 3x + 4$$

You will see functions labeled differently, $f(x)$, $g(x)$, $J(x)$.  This is just a way of labeling the function, similar to how we name our functions in code.  For example, we can assign:

$$ f(x) = 10x + 12 $$

$$ g(x) = x + 100 $$

Later on, we can reference the second function, $g(x)$, and know which function we're referring to.

### Functions depending on other functions

Now that we know how to label different functions, we can also take a look at what it means for functions to depend on other functions.  In code, we see this all of the time.  For example, here is a function that we have solved before.


```python
def squared_error(actual, expected):
    return (actual - expected)**2

squared_error(4, 2)
```




    4



But we can really break this function into two:


```python
def error(actual, expected):
    return actual - expected
    
def squared_error(actual, expected):
    return error(actual, expected)**2

squared_error(4, 2)
```




    4



In code, composing our functions from other functions helps us break down a problem.  It will be easier for us understand our code when we refer to it later on.  Similarly, functional composition in mathematics can also help break down problems and assist with readability.  Here is how we express it.  Let's represent the function `error` as $g(x, y) = x - y $, where $x$ represents actual and $y$ represents expected. 

$$g(x, y) = x - y  $$

Now we can represent squared error as the following.

$$ f(g(x, y)) = g(x, y) ^2 $$

Take a close look at this second function.  We are expressing that this second function, $f$, depends on $g(x, y)$ and thus also depends on $x$ and $y$.  The output of the function $f$ will vary according to a few inputs.  As we'll see soon, functional composition helps us break down some complex problems.  But really, we're just saying that to determine what $f(g(x,y))$ will output, we need to know the variables $x$ and $y$ as well as the function $g(x, y)$.  This relationship is similar to our `squared_error` function because we need to know the `error` function, as well as the arguments of `actual` and `expected`.  

Let's see one more example to make sure that we have the hang of it.  Take the following function:

$$z(x) = (3 + 4x)^2$$  

Now let's try to represent with functional composition.  How?  Here's one way:

$$f(x) = 3 + 4x $$ 

$$ g(f(x)) = f(x)^2 $$

### Summary

In this section, we learned about expressing functions mathematically.  We saw that when what we call a function, the letter we use,whether $f$ or $g$ or $z$, doesn't matter.  We only are giving our function a name that we easily can refer to later on.  In the parentheses, we indicate what the output of the function is dependent on.  Sometimes the output of the function depends on one variable, and sometimes our function depends on multiple variables.  Sometimes our function depends on another *function*, whose output depends on other variables.  

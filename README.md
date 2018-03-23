
# Being expressive with functions

### Learning objectives

* Understand what it means to say that a function is dependent on a variable
* Understand how to express a multivariable function 
* Understand how to express a function that is composed of another function, and why to express functions that way  

### Introduction

As we have seen, our concepts in mathematics and in code line up pretty nicely.  It's time we go off on a little bit of a tangent to explore how the way we denote functions in math lines up to how we denote functions in code. Through this, we will also learn different ways of denoting functions with math.  Some of these concepts may feel like review, but making sure we have a handle on them will give us clarity when we move on to explore other topics in mathematics.

### Expressing functions

So let's begin a way to talk about functions in general.  We describe a function as $f(x)$.  Now $f(x)$ is our generic way to express a function.  We are not saying the output equals $y$ or anything else, we are just saying that the function returns an output.  For example, we can say the following:

$$f(x) = 3x$$

The above just means that there is an output that equals 3 times $x$.  

Note that our mathematical expression of an output varying with an input lines up nicely to how a function varies with input.  To show that a function varies with an input, we just use an argument.


```python
def f(x):
    return 3*x
```

### Evaluating functions at specific values

Now let's evaluate the function $f(x)$ at specific values of $x$.  So when $x = 3$, $f(x) = 3x = 3*3 = 9$.  And when $x = 4$,  $f(x) = 4*3 = 12$.  Another way of saying "when $x = 3$ is simply to say $f(3)$.  So:
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



### Unpacking  the $x$ in  $f(x)$

So the $x$ part of $f(x)$ indicates that function produces different outputs with different values of $x$.  As our values of $x$ change, the output of the function changes.  By describing our function as $f(x)$, or a function of $x$ we also indicate that a specific input of $x$ always returns the same output from the function.  

Now take a look at another function:

$$ f = 3x + y$$

Now to determine this output, we need to know more than a specific value of $x$.  We also need to know the value of $y$.  So it's no longer the case that a specific input of $x$ always returns the same output from the function.  Rather specific inputs of $x$ and $y$ always returns the same output.  So we indicate this like so:

$$ f(x,y) = 3x + y$$


```python
def f(x,y):
    return 3*x + y
```

And to evaluate indicate that we are evaluating the function at specific values of $x$ and $y$, we write the following: 

$$ f(3,4) = 3*3 + 4 = 13$$


```python
f(3, 4)
```




    13



A function whose output depends on *multiple* variables, like $x$ and $y$ is called a **multivariable function**.

Now how would we express the function:

$$ f = 3x + 4$$

Is that a multi-variable function?  While the number 4 influences the output of the function, we do not need to know anything but the value of $x$ in order to determine the output of the function.  So we still would express that function as a single variable function:

$$ f(x) = 3x + 4$$

And in code:


```python
def f(x):
    return 3*x + 4
```

### Unpacking  the $f$ in  $f(x)$

So now that we understand the significance of $x$ in $f(x)$ what does the $f$ mean?  Well not too much.  It just a label for a specific function.  But we could have just as easily written our function as:

$$ g(x) = 3x + 4$$

You will see functions labeled differently, $f(x)$, $g(x)$ just as a way of what is what, similar to how we name specific functions in code.  So for example, we can assign:

$$ f(x) = 10x + 12 $$

$$ g(x) = x + 100 $$

And now in the future, we can just reference the second function as $g(x)$ and we know which function we're referring to.

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



In code, composing our functions from other functions helps us readability as well as break problems down.  Similarly, functional composition in mathematics can also help break down problems and assist with readability.  Here is how we express it.  Let's represent the function `error` as $g(x, y) = x - y $ where $x$ represents actual and $y$ represents expected. 

$$g(x, y) = x - y  $$

Now we can represent squared error as the following.

$$ f(g(x, y)) = g(x, y) ^2 $$

So now we are expressing that this second function, $f$ depends on $g(x, y)$ and also depends on $x$ and $y$.  So the output of the function will vary with a few things.  As you'll see soon, functional composition can help us just break down some problems.  But really, we're just saying that to determine what $f(g(x,y))$ will output, you need to know the variables $x$ and $y$ as well as the function $g(x, y)$.  Just like to know what our `squared_error` function will return, we need to know about our `error` function, as well as the arguments of `actual` and `expected`.  

Let's do one more to make sure we have the hang of it.  Take the following function:

$$z(x) = (3 + 4x)^2$$  

How could we represent this as multiple functions?  Here's one way:

$$f(x) = 3 + 4x $$ 

$$ g(f(x)) = f(x)^2 $$

### Summary

In this section, we learned about expressing functions mathematically.  We saw that when what we call a function, whether $f$ or $g$ or $z$ is used for identifying a function.  In the parentheses, we indicate what the output of the function is dependent on.  Sometimes the output of the function depends on one variable, sometimes multiple variables, and sometimes it depends on other functions, whose output depends on other variables.  

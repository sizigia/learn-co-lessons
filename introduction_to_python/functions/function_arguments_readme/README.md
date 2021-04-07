
# Function Arguments

### Introduction

Function arguments are a powerful tool in programming.  As we'll see, arguments make our functions more flexible and reusable by explicitly allowing different inputs to be used in a function and changing the output of the function based on these inputs.

When used correctly, function arguments bring clarity to what inputs a function needs to operate, as well as how a function uses these inputs.  

### Learning Objectives

* Understand how function arguments make functions more flexible and predictable
* Understand how to define and execute a function with arguments

### Predictability with arguments

In the previous lesson, we saw that functions were a powerful tool.  They allow us to repeat operations and apply these operations to different data.  For example, take a look at a function called `meet_traveller`.


```python
def meet_traveller(): 
    welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
    return welcome_message # return statement
```

The `meet_traveller` function is designed to generate nice greetings to each new employee.  Do we need anything else to run the function?  How do we know which new employee the function will greet?  Let's run the function and see what happens.


```python
meet_traveller()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-47-808d0f7c17d9> in <module>()
    ----> 1 meet_traveller()
    

    <ipython-input-46-70bd219b8158> in meet_traveller()
          1 def meet_traveller():
    ----> 2     welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
          3     return welcome_messages # return statement


    NameError: name 'traveller' is not defined


The function requires the variable `traveller`, but it's hard to tell that before running the function.  When code requires something to work, we call that something a **dependency**. Below, our function `meet` depends on the variable `traveller` being provided, or it will not work. Ideally, our dependencies are more explicit than in our `meet_traveller` function.  Let's adapt this function to make its dependencies more explicit.


```python
def meet(traveller): 
    welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
    return welcome_message
```

Ok, in the code above we changed the first line of the function, the function signature, to the following:

```def meet(traveller): ```

This tells us, and Python, to not even run the code unless the proper data to the function is provided.  Let's see it.


```python
meet()
```


    ----------------------------------------------------------------------

    TypeError                            Traceback (most recent call last)

    <ipython-input-2-c60a3be83cb4> in <module>()
    ----> 1 meet()
    

    TypeError: meet() missing 1 required positional argument: 'traveller'


Do you see that error message at the bottom there?  It's pretty explicit about saying that this argument requires a positional argument `traveller`.  

So, by using an argument, the function signature tells us how to run this function.  We refer to the function by it's name and then pass through a string representing the `traveller`.


```python
meet('sally')
```




    "Hi Sally, I'm so glad we'll be going on the trip together!"



### Flexibility

Let's take another look at the `meet` function. Notice, that the argument operates like a variable in that we can easily alter the data that `traveller` points to. When we pass through the string, `'Sally'`, the function replaces `traveller` with the string `'Sally'`.  


```python
def meet(traveller): 
                              # "sally"
    welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
    return welcome_message
```

And we can easily change what `traveller` points to just by passing through a different string.


```python
meet('fred')
```




    "Hi Fred, I'm so glad we'll be going on the trip together!"



But notice that the `traveller` argument is only accessible just inside of the function.


```python
traveller
```


    ----------------------------------------------------------------------

    NameError                            Traceback (most recent call last)

    <ipython-input-6-12a71905bbfe> in <module>()
    ----> 1 traveller
    

    NameError: name 'traveller' is not defined


So by using arguments, we can easily see what a function requires to work, change the output by passing through different data to the function, and ensure that we only have to worry about what our argument is while inside that function. 

### Summary

In this lesson, we saw some of the benefits of using arguments: they make our functions more flexible and predictable.  Our functions are more flexible as the functions vary based on the argument provided to the function.  Arguments make our functions predictable by making functions more explicit about their dependencies. They also allow us to change the value of an argument which only affects the functions internal values and more directly shows us how the output of our function will vary based on different inputs.    

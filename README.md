
# Function arguments

### Introduction

Function arguments allow our code to be even more descriptive.  When used correctly, they make our functions more predictable by being explicit about what a function needs to operate properly, as well as the impact that a function has.  They also make our functions more flexible by adjusting the output based on the input of the function.

### Learning Objectives

* Understand how function arguments make are functions more flexible and predictable
* Understand how to define a function with arguments
* Understand how to execute a function with arguments

### Predictability with arguments

In the previous lesson, we saw that functions were a powerful tool.  They allow us to repeat operations and apply these operations to different data.  For example, take a look at a function called `meet_traveller`.


```python
def meet_traveller(): 
    welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
    return welcome_message # return statement
```

That function is designed to generate nice greetings to each new employee.  Do we need anything else to run the function?  How do we know how to define which new employee to greet?  Let's run the function.


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


The function requires the variable `traveller`, but it's hard to tell that before running the function.  When code requires something to work, we call that something a **dependencies**.  Our function `meet` has a dependency on the variable `traveller` being provide, or it will not work. Ideally, our dependencies are more explicit.  Let's adapt this function to make the requirements of the function more clear.


```python
def meet(traveller): 
    welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
    return welcome_message
```

Ok, notice that we changed the first line of the function, the function signature to the following:

```def meet(traveller): ```

This tells us, and Python to not even run the code unless the proper data to the function is provided.  Let's see this!


```python
meet()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-55-a39c83f80042> in <module>()
    ----> 1 meet()
    

    TypeError: meet() missing 1 required positional argument: 'traveller'


Do you see that error message at the bottom there?  It's pretty explicit about saying that this argument requires a positional argument `traveller`.  And of course, we could have seen this, just by looking at the function signature.

```def meet(traveller): ```

So, by using an argument, the function signature tells us how to run this function: refer to the function by it's name and then pass through a string representing the `traveller`.


```python
meet('sally')
```




    "Hi Sally, I'm so glad we'll be going on the trip together!"



### Flexibility

So take another look at the function, the argument operates like a variable.  We can easily alter the data that `traveller` equals.  When we pass through the string, `'Sally'`, everytime the function references `traveller` it replaces it with the string `'Sally'`.  


```python
def meet(traveller): 
                              # "sally"
    welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
    return welcome_message
```

And we can easily change what this points to just by passing through a different string.


```python
meet('fred')
```




    "Hi Fred, I'm so glad we'll be going on the trip together!"



But this argument is only accessible just inside of the function.


```python
traveller
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-64-2dffa69ae56a> in <module>()
    ----> 1 traveller
    

    NameError: name 'traveller' is not defined


So by using arguments, we can easily see what a function requires to work, change the output of by passing through different data to the function, and ensure that we only have to worry about what our argument equals while inside that function. 

### Summary

In this lesson, we saw some of the benefits of using arguments: they make our functions more flexible and predictable.  Our functions are more flexible as the functions vary based on the argument provided to the function.  And arguments make our functions predictable by making functions more explicit about their dependencies, allow us to only change the value of an argument that stays internal to a function, and shows more directly how the output of our function will vary.    

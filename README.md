
# Functions lab

## Introduction

As we know, we can use functions to name sequences of our code, thus making our code more expressive. We can also use functions to allow us to reuse our code. In this lab we will practice using functions for these purposes.

## Objectives

* Practice declaring and returning values from functions
* Practice accessing variables that are outside of a function's scope, from inside of a function

## Writing our first functions

Imagine we are working on our list of travel destinations -- which is really turning out to be a full time job. We have our list of `travel_destinations` which we assign below. Write a function called `number_of_destinations` that returns the number of destinations we have on our list.


```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
def number_of_destinations():
    return len(travel_destinations)
```


```python
number_of_destinations() # 6
```




    6



Now write another function called `next_up` that returns our first destination (the destination with the lowest index), in the `travel_destinations` list.


```python
def next_up():
    return travel_destinations[0]
```


```python
travel_destinations = ['argentina', 'mexico', 'italy']
next_up() # 'argentina'
```




    'argentina'




```python
travel_destinations = ['finland', 'canada', 'croatia']
next_up() # 'finland'
```




    'finland'



Ok, now write a function called `favorite_destination` that returns the string `'madagascar'`.


```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
def favorite_destination():
    travel_destinations.append('madagascar')
    return travel_destinations[-1]
```


```python
favorite_destination() # 'madagascar'
```




    'madagascar'



Again, let's declare an array called `travel_destinations`. Change the function `favorite_destination` so that it continues to return the string `'madagascar'`, but also adds the string `'madagascar'` to the end of the list of destinations.


```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
favorite_destination()
travel_destinations[-1] # 'madagascar'
```




    'madagascar'



Now let's write another function which iterates through the list of `destinations` and capitalizes the first letter of each word. It should return a list of capitalized destinations.


```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
def capitalize_countries():
    capitalized_countries = []
    for destination in travel_destinations:
        capitalized_countries.append(destination.title())
    return capitalized_countries
```


```python
capitalize_countries() # ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia']
```




    ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia']



Great! Now if someone adds a country that is lowercased to our list of destinations, we can simply call our function again to capitalize each of the destinations in the list.


```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
capitalize_countries() # ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia']
travel_destinations.append('japan')
capitalize_countries() # ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia', 'Japan']
```




    ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia', 'Japan']



## Summary

Great job! In this lab we were able to get practice both writing and returning values from functions. We also practiced accessing variables not local to the function but in the global scope.

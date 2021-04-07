
## A quick glance at numbers

### Objectives
* Operating on numbers in Python
* The different datatypes for numbers
* Boolean values and how we can use them in our code
* Deciding which datatypes to use in our program

All of us are familiar with numbers.  1492 is a number.  So is 34.  If we think about what we usually do with numbers, we get a pretty good idea for what Python provides support for.


```python
1 + 1
# 2
```




    2




```python
2 * 5
# 10
```




    10



If we look at a number for its type, we find something slightly different.


```python
type(10)
# int
```




    int




```python
type(10.2)
# float
```




    float



Python is simply indicating that a number without a decimal is called an `int` for integer, and a number with a decimal is called a `float` (for "floating point"). For now, we can think of both of these as numbers, although later we'll have to learn about the complexities of doing math with floating point numbers.


```python
10 + 0.75
# 10.75
```




    10.75



As we can see in the above example, the `float`, `0.75`, plus the `int`, `10`, resolves to the `float`, `10.75`. 

### What is a boolean?

A boolean has two possible values: **True** or **False**.


```python
type(True)
# bool
```




    bool



It's fairly rare for programmers to explicitly write the word `True` or `False`.  Instead our programs can respond to questions for us in this form.  We have already seen one such example:


```python
"Homer Simpson".endswith("Simpson")
# True
```




    True




```python
"Homer Simpson".endswith("Homer")
# False
```




    False



And as you might imagine, a boolean can be returned from a math operation as well.


```python
3 * 5 < 10
# False
```




    False



You will see later on that by utilizing these returned booleans, we can make decisions with our code. For example: send this email if a user's last name is Simpson, or send an invite if the user is in a target age group. We aren't there yet, but we'll get there!

### Datatypes as a choice

> "Bad programmers worry about the code. Good programmers worry about data structures and their relationships." - Linus Torvald 

For now, it's interesting to think of how methods allow us to change between datatypes and to think of when we may want our data to be one datatype versus another.  We started this lesson by saying that 34 is a number.  But what if it's not?


```python
"west 34th street"
# 'west 34th street'
```




    'west 34th street'



We could make the argument that in certain contexts, like an address, it is text.  In others, when we are judging distance in blocks it feels like a number.  So how do we decide?  

The answer is by really thinking about what we want to do with the data.  If we want to capitalize all of the words in the string, to mail a letter (which I admit, sounds awful), we should keep the data in the format of a string.


```python
"34th street".title()
# '34th Street'
```




    '34Th Street'



What if we are trying to ask if a number in that string is larger than another number?  For example, a restaurant that only delivers food below 22nd street might use a program to write something like: 


```python
34 < 22
# False
```




    False



But would a method like less than ( `<` ) work with a string? Does it make sense for a string or text to answer whether it is less than or greater than a number? Trying things is free, so let's give it a shot.


```python
"34th street" < 22
# False
```




    False



Well, now we know for sure.  So, if we want to help our restaurant with deliveries, we should convert from a string to a number and then make the comparison.


```python
int('34') < 22
# False
```




    False



And if we want to go from a number to a string, for example to produce an address, we again need to pay attention to the type.


```python
str(34) + 'th Street'
# '34th Street'
```




    '34th Street'



Here we saw our first method for switching between types: simply write the name of the type followed by parentheses and the data on which we want to operate. After introducing this pattern, we can start to explore with others types such as the boolean.


```python
bool(100)
# True
```




    True




```python
bool(0)
# False
```




    False



Great, so we can coerce a number to a boolean as well.  And we are beginning to think about keeping our data in one form or another based on what we want to do with that data.    

### Summary

In this section, we introduced two new types of data: numbers and booleans. We saw that numbers allow us to perform standard math operations, and we saw that booleans answer whether something is True or False, and serve as a way our program or different methods can respond to questions.

We have seen almost all of our Python datatypes, we talked about how to choose a datatype, and we talked about how to switch between datatypes.  We said that we choose a datatype based on the capabilities that we want to give to that data: should it answer whether it is larger or smaller, or does it make sense to capitalize? The goal of this discussion is to begin thinking about why we decide to put data in specific types (i.e. string, number, boolean). We also introduced coercion methods like `bool` and `str` that coerce/force/switch between datatypes. 


## A quick glance at numbers

All of us are familiar with numbers.  1492 is a number.  So is 34.  And if you think about what you'd like to do with a number, you probably have a pretty strong guess of what Python allows you to do with numbers.


```python
1 + 1
```




    2




```python
2 * 5
```




    10



If you look ask a number for a type, you would find something slightly different.


```python
type(10)
```




    int




```python
type(10.2)
```




    float



But all python is indicating is that a number without a decimal is called an `int` for integer and a number with a decimal is called a `float`.  But you can move forward safely with just thinking of them as numbers and everything goes fine.


```python
3/4 + 10
```




    10.75



### And what is a boolean

A boolean is used to divide into two: True or False.


```python
type(True)
```




    bool



It's fairly rare for programmers to explicitly write the word `True` or `False`.  Instead our programs can respond to questions for us in this form.  We have already seen one such example:


```python
"Homer Simpson".endswith("Simpson")
```




    True




```python
"Homer Simpson".endswith("Homer")
```




    False



And as you might imagine, a boolean can be returned from a math operation as well.


```python
3 * 5 < 10
```




    False



You will see later on, that using these returned booleans, we can make decisions with our code.  Send this email if a user's name is Simpson, or send an invite if the user is in a target age group.  But we'll get there.

### Datatypes as a choice

> "Bad programmers worry about the code. Good programmers worry about data structures and their relationships." - Torvald 

For now, it's interesting to think of how methods allow us to change between datatypes.  And when we may want our data to be in one datatype versus another.  We started this lesson by saying that 34 is a number.  But what if it's not.


```python
"west 34th street"
```




    'west 34th street'



We could make the argument that in certain contexts, like an address, it is text.  In others, when we are judging distance in blocks it feels like a number.  So how do we decide?  

The answer is by really thinking about what we want to do with the data.  If we want to capitalize all of the words in the string, to mail a letter (which I admit, sounds awful), we should keep the data in the format of a string.


```python
"34th street".title()
```




    '34Th Street'



However, what if we are trying to ask if a number in that string is larger than another number.  For example, a restaurant that only delivers food below 22nd street might use a program to write something like: 


```python
34 < 22
```




    False



But would a method like less than, be in a string?  Does it make sense for a string, text, to answer whether it is less than or greater than something?  Trying things is free, so let's give it a shot.


```python
"34th street" < 22
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-41-08662b2a59f1> in <module>()
    ----> 1 "34th street" < 22
    

    TypeError: '<' not supported between instances of 'str' and 'int'


Well, now we know for sure.  So if we want to help our restaurant with deliveries, we should convert our number from a string to a number and then make the comparison.


```python
int('34') < 22
```




    False



And if we want to go from a number to the string, for example to produce an address, we again need to pay attention to the type.


```python
str(34) + 'th Street'
```




    '34th Street'



So here we saw our first method for switching between types: simply write the name of the type followed by parentheses and the data.  After identifying this pattern, we should really explore with our other type the boolean.


```python
bool(100)
```




    True




```python
bool(0)
```




    False



Great, so we can coerce a number to a boolean as well.  And we are beginning to think about keeping our data in one form or another based on what we want to do with that data.    

### Summary

In this section, we introduced two new types of data: numbers and booleans.  We saw that numbers allow us to perform standard math operations. And we saw that booleans answer whether something is True or False, and are a form of how our program or different methods can respond to questions.

Now that we have seen almost all of our Python datatypes, we talked about how to choose a datatype, and how to switch between datatypes.  We said that we choose a datatype based on the capabilities that we want to give to that data: should it answer whether it is larger or smaller, or does it make sense to capitalize?  We entered this discussion so you begin to think of what you are deciding when putting a data in a specific form.  We also talked about this so that you can begin to identify coercion methods like `bool` and `str` that switch us between datatypes. 

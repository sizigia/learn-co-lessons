
# Why use code

## Let's go

To answer questions with data, we need to programming for two main skills: representing the world with data, and operating on that data.  Or in other words, we need our code to **be something** or **do something**.  Let's just worry about being for now, we can hold off the doing part for later. 

### Objectives
* Working with our first datatype, strings
* Learning about methods that Python provides us
* Learning how to discover new methods

## Working with text

A lot of information in the world is in the form of text.  And if we want to capture this information, and operate on it we should become familiar with an entire datatype in Python dedicated to it: the string.


```python
'Homer Simpson'
```




    'Homer Simpson'



When programmers say "string", what they mean is text.  When programmers say datatype, they just mean type of data.  For example, here is another datatype in Python, a number.


```python
3
```




    3



We can discover the type of a piece of data by calling the `type` method.


```python
type('Homer Simpson')
```




    str



We pay attention to what type of data we are working with because they operate differently.

For example, to initialize a string we cannot simply type letters.  Instead, we need to be very explicit with Python and tell Python it is about to see some text.  We do this by surrounding our text with quotes.  If we don't do that, or end our quotation marks too early, Python will throw us an error.


```python
'Homer Simps'on
```


      File "<ipython-input-35-cfe60ad2684c>", line 1
        'Homer Simps'on
                      ^
    SyntaxError: invalid syntax



If you want, you can also use double quotes.


```python
"Homer don't care"
```




    "Homer don't care"



## Changing data with built in methods

The reason Python is so picky is because, once it knows we are working with a string, it gives us different functionality for operating on strings.  We call this functionality a function, or a method.

For example here is a method that works with a string (text), but does not work with a number.


```python
'Homer Simpson'.upper()
```




    'HOMER SIMPSON'




```python
42.upper()
```


      File "<ipython-input-17-ade3a24a9923>", line 1
        42.upper()
               ^
    SyntaxError: invalid syntax



Yep.  Bad news bears.

We can operate on a datatype with the following format: 

* datatype
* dot 
* method name
* parentheses

Here's another example. And as you can see, it follows the same format.


```python
"Homer Simpson".endswith('Simpson')
```




    True




```python
"Charles Montgomery Burns".endswith('Simpson')
```




    False



So as you can see, by following the format of data-dot-method name-parentheses we can begin to operate on our data.

###  Discovering new methods

You may be starting to worry about there being too many methods to keep track of.  Let's ask Python for help with finding more information about what we can do with strings.


```python
help('strings')
```

    No Python documentation found for 'strings'.
    Use help() to get the interactive help utility.
    Use help(str) for help on the str class.
    


The `help()` word with Python comes out of the box with the language, and is like an old school Alexa.  And just like Alexa, it often doesn't understand us.  Let's follow it's stern directions, and see what happens when we type in `help(str)`.


```python
help(str)
```

    Help on class str in module builtins:
    
    class str(object)
     |  str(object='') -> str
     |  str(bytes_or_buffer[, encoding[, errors]]) -> str
     |  
     |  Create a new string object from the given object. If encoding or
     |  errors is specified, then the object must expose a data buffer
     |  that will be decoded using the given encoding and error handler.
     |  Otherwise, returns the result of object.__str__() (if defined)
     |  or repr(object).
     |  encoding defaults to sys.getdefaultencoding().
     |  errors defaults to 'strict'.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(...)
     |      S.__format__(format_spec) -> str
     |      
     |      Return a formatted version of S as described by format_spec.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __sizeof__(...)
     |      S.__sizeof__() -> size of S in memory, in bytes
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  capitalize(...)
     |      S.capitalize() -> str
     |      
     |      Return a capitalized version of S, i.e. make the first character
     |      have upper case and the rest lower case.
     |  
     |  casefold(...)
     |      S.casefold() -> str
     |      
     |      Return a version of S suitable for caseless comparisons.
     |  
     |  center(...)
     |      S.center(width[, fillchar]) -> str
     |      
     |      Return S centered in a string of length width. Padding is
     |      done using the specified fill character (default is a space)
     |  
     |  count(...)
     |      S.count(sub[, start[, end]]) -> int
     |      
     |      Return the number of non-overlapping occurrences of substring sub in
     |      string S[start:end].  Optional arguments start and end are
     |      interpreted as in slice notation.
     |  
     |  encode(...)
     |      S.encode(encoding='utf-8', errors='strict') -> bytes
     |      
     |      Encode S using the codec registered for encoding. Default encoding
     |      is 'utf-8'. errors may be given to set a different error
     |      handling scheme. Default is 'strict' meaning that encoding errors raise
     |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
     |      'xmlcharrefreplace' as well as any other name registered with
     |      codecs.register_error that can handle UnicodeEncodeErrors.
     |  
     |  endswith(...)
     |      S.endswith(suffix[, start[, end]]) -> bool
     |      
     |      Return True if S ends with the specified suffix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      suffix can also be a tuple of strings to try.
     |  
     |  expandtabs(...)
     |      S.expandtabs(tabsize=8) -> str
     |      
     |      Return a copy of S where all tab characters are expanded using spaces.
     |      If tabsize is not given, a tab size of 8 characters is assumed.
     |  
     |  find(...)
     |      S.find(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  format(...)
     |      S.format(*args, **kwargs) -> str
     |      
     |      Return a formatted version of S, using substitutions from args and kwargs.
     |      The substitutions are identified by braces ('{' and '}').
     |  
     |  format_map(...)
     |      S.format_map(mapping) -> str
     |      
     |      Return a formatted version of S, using substitutions from mapping.
     |      The substitutions are identified by braces ('{' and '}').
     |  
     |  index(...)
     |      S.index(sub[, start[, end]]) -> int
     |      
     |      Like S.find() but raise ValueError when the substring is not found.
     |  
     |  isalnum(...)
     |      S.isalnum() -> bool
     |      
     |      Return True if all characters in S are alphanumeric
     |      and there is at least one character in S, False otherwise.
     |  
     |  isalpha(...)
     |      S.isalpha() -> bool
     |      
     |      Return True if all characters in S are alphabetic
     |      and there is at least one character in S, False otherwise.
     |  
     |  isdecimal(...)
     |      S.isdecimal() -> bool
     |      
     |      Return True if there are only decimal characters in S,
     |      False otherwise.
     |  
     |  isdigit(...)
     |      S.isdigit() -> bool
     |      
     |      Return True if all characters in S are digits
     |      and there is at least one character in S, False otherwise.
     |  
     |  isidentifier(...)
     |      S.isidentifier() -> bool
     |      
     |      Return True if S is a valid identifier according
     |      to the language definition.
     |      
     |      Use keyword.iskeyword() to test for reserved identifiers
     |      such as "def" and "class".
     |  
     |  islower(...)
     |      S.islower() -> bool
     |      
     |      Return True if all cased characters in S are lowercase and there is
     |      at least one cased character in S, False otherwise.
     |  
     |  isnumeric(...)
     |      S.isnumeric() -> bool
     |      
     |      Return True if there are only numeric characters in S,
     |      False otherwise.
     |  
     |  isprintable(...)
     |      S.isprintable() -> bool
     |      
     |      Return True if all characters in S are considered
     |      printable in repr() or S is empty, False otherwise.
     |  
     |  isspace(...)
     |      S.isspace() -> bool
     |      
     |      Return True if all characters in S are whitespace
     |      and there is at least one character in S, False otherwise.
     |  
     |  istitle(...)
     |      S.istitle() -> bool
     |      
     |      Return True if S is a titlecased string and there is at least one
     |      character in S, i.e. upper- and titlecase characters may only
     |      follow uncased characters and lowercase characters only cased ones.
     |      Return False otherwise.
     |  
     |  isupper(...)
     |      S.isupper() -> bool
     |      
     |      Return True if all cased characters in S are uppercase and there is
     |      at least one cased character in S, False otherwise.
     |  
     |  join(...)
     |      S.join(iterable) -> str
     |      
     |      Return a string which is the concatenation of the strings in the
     |      iterable.  The separator between elements is S.
     |  
     |  ljust(...)
     |      S.ljust(width[, fillchar]) -> str
     |      
     |      Return S left-justified in a Unicode string of length width. Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  lower(...)
     |      S.lower() -> str
     |      
     |      Return a copy of the string S converted to lowercase.
     |  
     |  lstrip(...)
     |      S.lstrip([chars]) -> str
     |      
     |      Return a copy of the string S with leading whitespace removed.
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  partition(...)
     |      S.partition(sep) -> (head, sep, tail)
     |      
     |      Search for the separator sep in S, and return the part before it,
     |      the separator itself, and the part after it.  If the separator is not
     |      found, return S and two empty strings.
     |  
     |  replace(...)
     |      S.replace(old, new[, count]) -> str
     |      
     |      Return a copy of S with all occurrences of substring
     |      old replaced by new.  If the optional argument count is
     |      given, only the first count occurrences are replaced.
     |  
     |  rfind(...)
     |      S.rfind(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  rindex(...)
     |      S.rindex(sub[, start[, end]]) -> int
     |      
     |      Like S.rfind() but raise ValueError when the substring is not found.
     |  
     |  rjust(...)
     |      S.rjust(width[, fillchar]) -> str
     |      
     |      Return S right-justified in a string of length width. Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  rpartition(...)
     |      S.rpartition(sep) -> (head, sep, tail)
     |      
     |      Search for the separator sep in S, starting at the end of S, and return
     |      the part before it, the separator itself, and the part after it.  If the
     |      separator is not found, return two empty strings and S.
     |  
     |  rsplit(...)
     |      S.rsplit(sep=None, maxsplit=-1) -> list of strings
     |      
     |      Return a list of the words in S, using sep as the
     |      delimiter string, starting at the end of the string and
     |      working to the front.  If maxsplit is given, at most maxsplit
     |      splits are done. If sep is not specified, any whitespace string
     |      is a separator.
     |  
     |  rstrip(...)
     |      S.rstrip([chars]) -> str
     |      
     |      Return a copy of the string S with trailing whitespace removed.
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  split(...)
     |      S.split(sep=None, maxsplit=-1) -> list of strings
     |      
     |      Return a list of the words in S, using sep as the
     |      delimiter string.  If maxsplit is given, at most maxsplit
     |      splits are done. If sep is not specified or is None, any
     |      whitespace string is a separator and empty strings are
     |      removed from the result.
     |  
     |  splitlines(...)
     |      S.splitlines([keepends]) -> list of strings
     |      
     |      Return a list of the lines in S, breaking at line boundaries.
     |      Line breaks are not included in the resulting list unless keepends
     |      is given and true.
     |  
     |  startswith(...)
     |      S.startswith(prefix[, start[, end]]) -> bool
     |      
     |      Return True if S starts with the specified prefix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      prefix can also be a tuple of strings to try.
     |  
     |  strip(...)
     |      S.strip([chars]) -> str
     |      
     |      Return a copy of the string S with leading and trailing
     |      whitespace removed.
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  swapcase(...)
     |      S.swapcase() -> str
     |      
     |      Return a copy of S with uppercase characters converted to lowercase
     |      and vice versa.
     |  
     |  title(...)
     |      S.title() -> str
     |      
     |      Return a titlecased version of S, i.e. words start with title case
     |      characters, all remaining cased characters have lower case.
     |  
     |  translate(...)
     |      S.translate(table) -> str
     |      
     |      Return a copy of the string S in which each character has been mapped
     |      through the given translation table. The table must implement
     |      lookup/indexing via __getitem__, for instance a dictionary or list,
     |      mapping Unicode ordinals to Unicode ordinals, strings, or None. If
     |      this operation raises LookupError, the character is left untouched.
     |      Characters mapped to None are deleted.
     |  
     |  upper(...)
     |      S.upper() -> str
     |      
     |      Return a copy of S converted to uppercase.
     |  
     |  zfill(...)
     |      S.zfill(width) -> str
     |      
     |      Pad a numeric string S with zeros on the left, to fill a field
     |      of the specified width. The string S is never truncated.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  maketrans(x, y=None, z=None, /)
     |      Return a translation table usable for str.translate().
     |      
     |      If there is only one argument, it must be a dictionary mapping Unicode
     |      ordinals (integers) or characters to Unicode ordinals, strings or None.
     |      Character keys will be then converted to ordinals.
     |      If there are two arguments, they must be strings of equal length, and
     |      in the resulting dictionary, each character in x will be mapped to the
     |      character at the same position in y. If there is a third argument, it
     |      must be a string, whose characters will be mapped to None in the result.
    


Holy cow that's a lot of words.  If we scroll down to the word capitalize, things begin to make more sense.  For example, for capitalize, this is what it says


capitalize(...)

    S.capitalize() -> str
    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.

Our next step is to use our formula of datatype-dot-method name-parentheses, and see what happens next.


```python
"smithers".capitalize()
```




    'Smithers'



Excellent.  Just like we thought.

### Tips going forward 

That's really it for this lesson on strings, and it's easy to feel a little unsatisfied with just a few methods on the datatype.  What's more important with programming is mechanisms of discovery and experimentation beyond just memorizing a list of features.

In this lesson, we already saw a few of them.  
* Guess: We just tried something and looked to the error message for clues as to what to do next.
* help(str): We saw a nice way to learn about new methods, then we took a guess to test our understanding
* Following a pattern: We started with a simple method like calling upper, took a moment to break this down into a pattern, and then tried this pattern again to call other methods 

Here is one more.  Just ask Google.  For example, look what happens when we ask Google about capitalization.

![](./ask-google.png)

A great link with a detailed answer.

![](./stack-overflow.png)

Then we try this new method out ourselves, to see if this user on StackOverFlow is right (they normally are).


```python
"hello world".title()
```




    'Hello World'



And our work is done.

### Summary

In this lesson, we learned about our first datatype in Python: strings.  A string is just text.  And we indicate to Python that we are writing a string by surrounding our content with quotation marks.  Once we do this, we can operate on this string by calling methods like `upper` or `endswith`.  We identified a general pattern for calling methods on datatypes: 'datatype-method name-dot-parentheses'.

The second thing we learned was different mechanisms for learning about methods.  We saw the importance of guessing and experimentation, and how doing so can give us error messages, which provide clues. We also saw how to ask questions about a datatype by calling 'help' followed by the datatype name like `help(str)`.  Finally, we saw we can ask Google.  This mechanism of exploration is a skill we'll build up over time and this course will provide guidance and practice on along the way.

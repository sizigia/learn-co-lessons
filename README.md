
# Visualizing Data

### Learning Objectives

* Understand the components of a point in a graph, an $x$ value, and a $y$ value 
* Understand how to plot a point on a graph, from a point's $x$ and $y$ value
* Get a sense of how to use a graphing library, like Plotly, to answer questions about our data

### Introduction

We have spent the last few sections introducing ourselves to various data structures in Python - from strings, integers and booleans, to collections like lists, and dictionaries.  In this section, we will see how, with the help of library, we can use these same data structures to display our data.

### Visualizing Data with Graphs

As we can see, in our list of cities, each city has a population number.  And we can display these various populations in a bar chart.

### Working with Plotly

To display our data, there are various Python visualization tools.  We prefer Plotly, as it produces nice looking graphs and is easy to work with.  

We can easily download the `plotly` library with the use of `pip`.  

> Pip is a package management system that allows us to easily download and install libraries written in Python.  If you are working in on Learn, we have already installed pip for you.  We will not walk through installing pip here, however you can find instructions on installing pip [for Mac](./http://softwaretester.info/install-and-upgrade-pip-on-mac-os-x/) or [for Windows](https://www.youtube.com/results?search_query=instally+pip+windows) online.


To install a package with pip, the general pattern is to run `pip install` and the name of the package.  We generally do this from a terminal (whatever that is), but you can also instally packages directly from Jupyter, like so.  (You can politely ignore any messages below that say requirement already satisfied.)


```python
!pip install plotly
```

    Requirement already satisfied: plotly in /Users/flatironschool/anaconda/lib/python3.6/site-packages
    Requirement already satisfied: pytz in /Users/flatironschool/anaconda/lib/python3.6/site-packages (from plotly)
    Requirement already satisfied: nbformat>=4.2 in /Users/flatironschool/anaconda/lib/python3.6/site-packages (from plotly)
    Requirement already satisfied: requests in /Users/flatironschool/.local/lib/python3.6/site-packages (from plotly)
    Requirement already satisfied: decorator>=4.0.6 in /Users/flatironschool/anaconda/lib/python3.6/site-packages (from plotly)
    Requirement already satisfied: six in /Users/flatironschool/anaconda/lib/python3.6/site-packages (from plotly)
    Requirement already satisfied: certifi>=2017.4.17 in /Users/flatironschool/.local/lib/python3.6/site-packages (from requests->plotly)
    Requirement already satisfied: urllib3<1.23,>=1.21.1 in /Users/flatironschool/.local/lib/python3.6/site-packages (from requests->plotly)
    Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /Users/flatironschool/anaconda/lib/python3.6/site-packages (from requests->plotly)
    Requirement already satisfied: idna<2.7,>=2.5 in /Users/flatironschool/anaconda/lib/python3.6/site-packages (from requests->plotly)


Now we have `plotly` on our computer.  The next step is to get it into this notebook.  We do so with the following two lines.


```python
import plotly

plotly.offline.init_notebook_mode(connected=True)
# use offline mode to avoid initial registration
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>


We bring in the `plotly` library by using the keyword `import` followed by our library name, `plotly`.  Then we call the method `plotly.offline.init_notebook_mode(connected=True)` so that we do not have to connect plotly to a registered account online.  If you are wondering how to get this knowledge, you simply ask Google.

![](./plotly-no-account.png)

Ok, now let's get to try to use plotly to build our first graph.  This is what we do.

We create new dictionary and assign it equal to `trace0`.    Then we set `x` key that points to a list of $x$ values.  Similarly, we create a `y` key with a value of a list of $y$ values.  


```python
trace0 = dict(x=['jack', 'jill', 'sandy'], y=[8, 11, 8, 13, 6, 4], type='bar')
trace0
```




    {'type': 'bar', 'x': ['jack', 'jill', 'sandy'], 'y': [8, 11, 8, 13, 6, 4]}



We plot our graph by calling the `plotly.offline.iplot` method and passing through a list of traces to `iplot` method.


```python
trace0 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy'], 'y': [8, 11, 8, 13, 6, 4]}


plotly.offline.iplot([trace0])
```


<div id="9147aaa1-2c92-4d84-b34d-17e2b70c4368" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("9147aaa1-2c92-4d84-b34d-17e2b70c4368", [{"type": "bar", "x": ["jack", "jill", "sandy"], "y": [8, 11, 8, 13, 6, 4]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


It may be confusing what a trace is, and how it is different from a plot.  The easiest way to explain is to have the `iplot` method taking an list of two traces, instead of just one.


```python
trace0 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy'], 'y': [8, 11, 8, 13, 6, 4]}
trace1 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy'], 'y': [4, 12, 3, 14, 8, 1]}


plotly.offline.iplot([trace0, trace1])
```


<div id="d31d4b95-8396-44f2-b4ba-83ab0a5fd290" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("d31d4b95-8396-44f2-b4ba-83ab0a5fd290", [{"type": "bar", "x": ["jack", "jill", "sandy"], "y": [8, 11, 8, 13, 6, 4]}, {"type": "bar", "x": ["jack", "jill", "sandy"], "y": [4, 12, 3, 14, 8, 1]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


So as you can see, each trace is an associated collection of data.

### Summary

In this section, we saw how we use data visualisations to better understand the data.

To display the data with `plotly` we need to do a couple of things.  First, we install plotly by going to our terminal and running `pip install plotly`.  Then to use the library, we import the `plotly` library into our notebook.  Once the library is loaded in our notebook, it's time to use it.  We create a new dictionary with keys of $x$ and $y$, with each key pointing to an array of the $x$ or $y$ values of our points.  We can pass through a list of traces, which each trace representing associated data.

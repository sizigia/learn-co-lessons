
# Visualizing Data

### Learning Objectives

* Get a sense of how to use a graphing library, like Plotly, to answer questions about how to visualize our data
* Understand how our dictionary and list data structures can represent graphical information

### Introduction

We have spent the last few sections introducing ourselves to various data structures in Python.  In this section, we will see how we can use these same data structures to display our data with the help of a library, Plotly.

### Working with Plotly

There are various Python visualization tools we can use to display our data. In this lesson, we will be using Plotly, as it produces nice looking graphs and is easy to work with.  

We can easily download the `plotly` library with the use of `pip`.  

> Pip is a package management system that allows us to easily download and install libraries written in Python.  If you are working on Learn, we have already installed pip for you.  We will not walk through installing pip here, however you can find instructions on installing pip [for Mac](http://softwaretester.info/install-and-upgrade-pip-on-mac-os-x/) or [for Windows](https://www.youtube.com/results?search_query=instally+pip+windows) online.  Also, if you are familiar with working with a terminal and have `easy_install`, you can run `sudo easy_install pip` from the terminal.

To install a package with pip, the general pattern is to run `pip install` followed by the name of the package.  We generally do this from a terminal (whatever that is), but you can also install packages directly from Jupyter, like so:

>**Note:** *You can ignore any messages below that say requirement already satisfied.*


```python
!pip install plotly
```

> Remember to use shift + enter to run the line above.

Now we have `plotly` on our computer.  The next step is to get it into this notebook.  We do so with the following two lines.


```python
import plotly

plotly.offline.init_notebook_mode(connected=True)
# use offline mode to avoid initial registration
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>


In the code above, we bring in the `plotly` library by using the keyword `import` followed by our library name, `plotly`.  Then we call the method `plotly.offline.init_notebook_mode(connected=True)` so that we do not have to connect plotly to a registered account online.  If you are wondering how to we know all of this, you simply ask Google.

![](./plotly-no-account.png)

Ok, now let's use plotly to build our first graph.

First, we create a new dictionary and assign it to `trace0`. Then we set `x` key that points to a list of $x$ values.  Similarly, we create a `y` key with a value of a list of $y$ values.  


```python
trace0 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy'], 'y': [8, 11, 10]}
trace0
```

Now we plot our graph by calling the `plotly.offline.iplot` method and passing through a list of traces to `iplot` method.


```python
import plotly

plotly.offline.init_notebook_mode(connected=True)
trace0 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy'], 'y': [8, 11, 10]}


plotly.offline.iplot([trace0])
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



<div id="ae2b19bc-c7f7-465c-8a73-ee614ba601fb" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("ae2b19bc-c7f7-465c-8a73-ee614ba601fb", [{"type": "bar", "x": ["jack", "jill", "sandy"], "y": [8, 11, 10]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


It may be confusing understanding what a trace is, and how it is different from a plot. The easiest way to explain it is maybe to show how the `iplot` method takes in a list of two traces, instead of just one.


```python
trace0 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy', 'blaise'], 'y': [8, 11, 8, 13, 6, 4]}
trace1 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy', 'gob'], 'y': [4, 12, 3, 14, 8, 1]}


plotly.offline.iplot([trace0, trace1])
```


<div id="7606a8a6-d17e-454f-b5e2-b1f326d55f63" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("7606a8a6-d17e-454f-b5e2-b1f326d55f63", [{"type": "bar", "x": ["jack", "jill", "sandy", "blaise"], "y": [8, 11, 8, 13, 6, 4]}, {"type": "bar", "x": ["jack", "jill", "sandy", "gob"], "y": [4, 12, 3, 14, 8, 1]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


As we can see, each trace is an associated collection of data, and a plot can display more than one trace.

### Summary

In this section, we saw how to use data visualizations to better understand the data.

To display the data with `plotly` we need to do a couple of things.  First, we installed plotly by going to our terminal and running `pip install plotly`.  Then to use the library, we import the `plotly` library into our notebook.  Once the library is loaded in our notebook, it's time to use it.  We create a new dictionary with keys of $x$ and $y$, with each key pointing to an array of the $x$ or $y$ values of our points.  We can pass through a list of traces, with each trace representing associated data.

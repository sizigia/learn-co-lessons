
# Visualizing Data with Graphs

### Introduction

In the previous section, we introduced all of the basic Python tools: datatypes, variables, data collections like lists and dictionaries, functions, loops, and iterators.  We will use these skills throughout our data science career.

Let's step back and take a look from the macro perspective.  The machine learning process is generally as follows:

* Gather and clean the data 
* Study the data
* Select a model 
* Train: Optimize the model for some other criteria (eg. how well the model predicts our known labeled data)
* Use the model predict on new data

The tools we learned in the previous section will help us gather and clean data.  We touched on studying the data with visualizations using the Plotly library in the previous section, but now it's time to take a deeper dive into exploring data with visualizations.

### Learning Objectives

* Understand the components of a point in a graph, an $x$ value, and a $y$ value 
* Understand where to place a point on a graph, from knowing a point's $x$ and $y$ value
* Get a sense of how to use a graphing library, like Plotly, to answer questions about our data

### A common problem

Imagine that Molly is selling cupcakes out of her kitchen.  She gains more and more customers, so she decides to hire a delivery person, Bob.  Molly asks us to calculate which customers are closest to and furthest from Bob.  This way, she can pay him appropriately.

Molly gives us a list of all of the customer locations, along with Bob's.  Here they are:

| Name | Avenue #| Block # | 
|------|------| ------     |
| Bob    | 4  |     8     | 
| Suzie  | 1  |     11     | 
| Fred   | 5  |     8     | 
| Edgar  | 6  |     13     | 
| Steven | 3  |     6     | 
| Natalie| 5  |     4     | 

Now to determine the person closest to Bob you decide to make a graph of each customer's locations, as well as Bob's, in a graph.

### Visualizing Data with Graphs

Before plotting everyone's locations, let's start off with a scatter plot of just one random point, the point $(2, 1)$.

![](./plot-one-point.png)

Ok so that graph above uses the cartesian coordinate system.  The coordinate system is used to display data along both an x-axis and y-axis.  The **x-axis** runs horizontally, from left to right, and you can see it as the labeled gray line along the bottom.  The **y-axis** runs vertically, from the bottom to the top.  You can see it labeled on the far left of our graph.

In the graph above, it shows the x-axis starting at -4 and the y-axis starting at -1, but that's just to make things easy to see.  In reality, you can imagine the x-axis and y-axis both including all numbers from negative infinity to positive infinity.  And that blue marker in top right portion of our graph represents the point where $x = 2 $ and $y = 1$.  Do you see why?  Well it's the place where the $x$ value is $2$, and the $y$ value is $1$.  As a shorthand, we mathematicians express this point as $(2, 1)$.  So the format is $(x, y) $, with the $x$ coordinate always coming first.

The light-gray lines form a grid on the graph to help us see where any given **point** is on a graph.  A point in geometry just means a location.  Now, test your knowledge by moving your mouse to the point $(4, 2)$.  Did you get it?  It's the spot at the top right of the graph.

### Plotting our data

Ok, now let's plot the data given.  


| Name | Avenue #| Block # | 
|------|------| ------     |
| Bob    | 4  |     8     | 
| Suzie  | 1  |     11     | 
| Fred   | 5  |     8     | 
| Edgar  | 6  |     13     | 
| Steven | 3  |     6     | 
| Natalie| 5  |     4     | 


We cannot graph the data with python itself, so we need to download a library from the Internet.  This is easy enough.  Simply go to your terminal and type in `pip install plotly` followed by the enter key.  Or you can press shift enter on the cell below.  If you already have `plotly` installed, you will see a message saying that it's already installed -- which you can safely ignore.


```python
!pip install plotly
```

Now we have `plotly` on our computer.  The next step is to apply it to this notebook.  We do so with the following two lines.


```python
import plotly

plotly.offline.init_notebook_mode(connected=True)
# use offline mode to avoid initial registration
```

We bring in the `plotly` library by using the keyword `import` followed by our library name, `plotly`.  We create a new dictionary in python with the `dict` constructor.  Then we pass through **named arguments** to the constructor to create a dictionary with an $x$ key that points to a list of $x$ values.  Similarly, we create a $y$ key with a value of a list of $y$ values. Note that the $x$ values match avenue numbers and the $y$ values match the block numbers.  We display this data by assigning our dictionary to the variable of `trace0`, and passing it through as an argument to the `plotly.offline.iplot` method.  


```python
import plotly
plotly.offline.init_notebook_mode(connected=True)
# we repeat these first lines just to keep the code together  

trace0 = dict(x=[4, 1, 5, 6, 3, 2], y=[8, 11, 8, 13, 6, 4])

# All that, and it doesn't even look good :(
plotly.offline.iplot([trace0])
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



<div id="7ced2553-80d5-423b-8431-769638f32d3f" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("7ced2553-80d5-423b-8431-769638f32d3f", [{"x": [4, 1, 5, 6, 3, 2], "y": [8, 11, 8, 13, 6, 4]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


The points were plotted correctly, but they are connected by a line, which doesn't represent anything in particular.

The lines are getting in the way.  Let's remove all of the connecting lines by setting `mode = "markers"`.  Then, let's also set labels to each of the dots, by setting `text` equal to a list of our names.  


```python
trace1 = dict(x=[4, 1, 5, 6, 3, 2],
              y=[8, 11, 8, 13, 6, 4], 
              mode="markers", 
              text=["bob", "suzie", "fred", "edgar", "steven", "natalie"],)


plotly.offline.iplot([trace1])

# much better :)
```


<div id="89a3bef8-0617-4e87-a9e4-df420522fd1f" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("89a3bef8-0617-4e87-a9e4-df420522fd1f", [{"x": [4, 1, 5, 6, 3, 2], "y": [8, 11, 8, 13, 6, 4], "mode": "markers", "text": ["bob", "suzie", "fred", "edgar", "steven", "natalie"]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Ok, so if you move your mouse over the dots, you can see the names that correspond to each point.  Also, when we hover over the dot at the x axis of point four, we can see that is Bob's point, just like it should be.  Now, who is closest to Bob?  It looks like Fred is closest since he's only one avenue away. Fred seems to be the easiest delivery for Bob.

### Summary

In this section, we saw how we use data visualizations to better understand the data.  A cartesian coordinate system nicely represents two dimensional data.  It allows us to represent a point's $x$ value by placing the point horizontally at the correct spot on the x-axis.  It represents a point's $y$ value by placing the point at the correct spot along the y-axis.

To display the data with `plotly` we need to do a couple of things.  First, we install plotly by going to our terminal and running `pip install plotly`.  Then to use the library, we import the `plotly` library into our notebook.  Once the library is loaded in our notebook, it's time to use it.  We create a new dictionary with keys of $x$ and $y$, with each key pointing to a list of the $x$ or $y$ values of our points.  To clean up the appearance we set the `mode` attribute equal to `'markers'`.

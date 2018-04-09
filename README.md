
# Applying Nearest Neighbors 

### Introduction

In the last lesson we derived the nearest neighbor formula.  Nearest neighbors is a powerful algorithm because it is based on the premise that data that based on proximity, we can predict other attributes about an individual.  For example, those who live in a particular neighborhood may be more likely to be a particular age, or have a similar neighborhood, and just based on proximity we can then see if their likelihood to purchase a product approximates that of their neighbors.

In this lesson we'll see how the nearest neighbors algorithm allows us to make predictions with data.  In doing so we'll also see our workflow for machine learning in general.  And we will see some common struggles that we have when applying a machine learning algorithm. 

###  Learning Objectives

* See the machine learning process of Collect, Explore, Train, and Predict 
* Use the nearest neighbors algorithm to predict other information about users
* See common tensions with machine learning algorithms

### Explore the data (again)

Once again, here are the locations of Bob and our customers.  This time let's add a fourth column for the number of purchases per year.

| Name | Avenue #| Block # | No. Purchases |
|------|------| ------     |  
| Bob    | 4  |     8     | 52
| Suzie  | 1  |     11     | 70
| Fred   | 5  |     8     | 60
| Edgar  | 6  |     13     | 20
| Steven | 3  |     6     | 32
| Natalie| 5  |     4     | 45

And we represent these individuals along with their yearly purchases in Python with the following:


```python
neighbors = [{'name': 'Bob', 'x': 4, 'y': 8, 'purchases': 52}, {'name': 'Suzie', 'x': 1, 'y': 11, 'purchases': 70}, 
             {'name': 'Fred', 'x': 5, 'y': 8, 'purchases': 60}, {'name': 'Edgar', 'x': 6, 'y': 13, 'purchases': 20},
             {'name': 'Steven', 'x': 3, 'y': 6, 'purchases': 32}, {'name': 'Natalie', 'x': 5, 'y': 4, 'purchases': 45}]
bob = neighbors[0]
suzie = neighbors[1]
```


```python
import plotly

plotly.offline.init_notebook_mode(connected=True)
trace0 = dict(x=list(map(lambda neighbor: neighbor['x'],neighbors)), 
              y=list(map(lambda neighbor: neighbor['y'],neighbors)),
              text=list(map(lambda neighbor: neighbor['name'] + ': ' + str(neighbor['purchases']),neighbors)),
              mode='markers')
plotly.offline.iplot(dict(data=[trace0], layout={'xaxis': {'dtick': 1}, 'yaxis': {'dtick': 1}}))
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



<div id="7baaf59c-d61d-478e-b331-07b065fe4225" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("7baaf59c-d61d-478e-b331-07b065fe4225", [{"x": [4, 1, 5, 6, 3, 5], "y": [8, 11, 8, 13, 6, 4], "text": ["Bob: 52", "Suzie: 70", "Fred: 60", "Edgar: 20", "Steven: 32", "Natalie: 45"], "mode": "markers"}], {"xaxis": {"dtick": 1}, "yaxis": {"dtick": 1}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


So looking at this data, the proximity of customers does seem to be a good indicator of the number of purchases of a customer.  For example, assume that a new customer just purchased his first cupcake, and we want to develop some expectation for how many cupcakes he may purchase from us in the next year.  His location may be a good indicator of this.  Let's see this what the nearest neighbors formula will tell us.

### Apply our nearest neighbors algorithm

Once again, here is our nearest neighbors algorithm.  The code below reflects the following steps:

1. Write a function to calculate the distance of one neighbor from another
2. Write a function that returns the distance between one neighbor and all others (using `map`)
3. Return a selected number of nearest neighbors

Ok once again, here is the code.


```python
import math

def distance(selected_individual, neighbor):
   distance_squared = (neighbor['x'] - selected_individual['x'])**2 + (neighbor['y'] - selected_individual['y'])**2
   return math.sqrt(distance_squared)

def distance_between_neighbors(selected_individual, neighbor):
    neighbor_with_distance = neighbor.copy()
    neighbor_with_distance['distance'] = distance(selected_individual, neighbor)
    return neighbor_with_distance

def distance_all(selected_individual, neighbors):
    remaining_neighbors = filter(lambda neighbor: neighbor != selected_individual, neighbors)
    return list(map(lambda neighbor: distance_between_neighbors(selected_individual, neighbor), remaining_neighbors))
```


```python
def nearest_neighbors(selected_individual, neighbors, number = None):
    number = number or len(neighbors)
    neighbor_distances = distance_all(selected_individual, neighbors)
    sorted_neighbors = sorted(neighbor_distances, key=lambda neighbor: neighbor['distance'])
    return sorted_neighbors[:number]
```


```python
bob = neighbors[0]
nearest_neighbor_to_bob = nearest_neighbors(bob, neighbors, 1)
nearest_neighbor_to_bob
```




    [{'distance': 1.0, 'name': 'Fred', 'purchases': 60, 'x': 5, 'y': 8}]



So for example, we try our `nearest_neighbors` function on a known piece of data, `bob`.  When we ask our function to just return the closest neighbor, then it returns Fred as the closest neighbor and estimates that Bob's number of purchases will be akin to his.  We can also apply the function to a customer at new location.


```python
nearest_neighbor_to_new = nearest_neighbors({'x': 4, 'y': 3}, neighbors, 1)
nearest_neighbor_to_new
```




    [{'distance': 1.4142135623730951,
      'name': 'Natalie',
      'purchases': 45,
      'x': 5,
      'y': 4}]



Just choosing the **nearest neighbor** seems pretty arbitrary for making an estimated purchase.  Our estimate will be determined just by one individual's purhcases.  To fix this, we can expand the number of neighbors and then take the average of their purchases to arrive at an estimate number for someone at that location.


```python
nearest_three_neighbors = nearest_neighbors({'x': 4, 'y': 3}, neighbors, 3)
nearest_three_neighbors
```




    [{'distance': 1.4142135623730951,
      'name': 'Natalie',
      'purchases': 45,
      'x': 5,
      'y': 4},
     {'distance': 3.1622776601683795,
      'name': 'Steven',
      'purchases': 32,
      'x': 3,
      'y': 6},
     {'distance': 5.0, 'name': 'Bob', 'purchases': 52, 'x': 4, 'y': 8}]




```python
purchases = list(map(lambda neighbor: neighbor['purchases'],nearest_three_neighbors))
average = sum(purchases)/len(purchases)
average # 43.0
```




    43.0



### Choosing the number of neighbors

Ok, so in the above section our nearest neighbors formula is making a prediction.  It's telling us that someone who lives on 4th street and 3rd Avenue would expect to make 45 purchases.  If you are feeling that this prediction approach is a little unscientific, that's a fair thought.  Our algorithm will change dramatically based on the number of nearest neighbors that we choose.  The number of neighbors that we choose in the nearest neighbors algorithm is called `k`.  No one knows why.

Choosing the correct number of neighbors to consider touches upon a number of themes in data science.  We'll visit these briefly here, not so that you walk away fully versed in all of them, but so that you are aware of them as you visit other machine learning problems.  

#### Underfitting

**Underfitting** occurs when our formula does not pick up on the relevant signals from the data.  For example, if the number of neighbors we have is too large, then our algorithm would improperly predict the purchases of our known customers, as it would not respond to differences in location.  

#### Minimizing for error

How do we know the correct number for k, that is number of neighbors to consider?  Well one way is to see how well our algorithm predicts our existing data, and then optimize for that.  

So for example, we see that our with k = 1, uses the nearest neighbor to Bob to predict 60 purchases for Bob, where Bob actually purchases 52.  So our formula is off by 8.  This number, our actual minus the expected, is called our **error**.  So we can add up how much our formula is off across all of our neighbors, and choose the k that minimizes the error for all of our data.

#### Training 

This approach of looking at our existing dataset optimizing for some metric, like a low error, is called **training**. Here we are training our algorithm by choosing numbers of k such that our algorithm optimizes for predicting the number of purchases in our dataset.

#### Overfitting

However, from training our algorithm to match our data, **overfitting** can occur.  Overfitting occurs when we overgeneralize from the data.  For example, if we are served a bad meal at a chain restaurant, we could improperly conclude that all meals at the restaurant are bad.  The same thing can happen with our algorithm.

Our algorithm can be optimized for and perform well with our existing data, but not do well with new data.  Imagine that we have one hundred cupcake customers and choosing a k of 2 accurately best minimizes the error in predicting the number of purchases.  We could find later that, as we get new customers, our model does not predict their purchases.

A problem could be that picked up on things that are particular to our data set, but will not generalize to new data.

#### Testing 

To see if the algorithm fits new data, we should try it with new data.  We do not want to wait for this new data to just arrive, so instead data scientists split their data into two: about 80 percent for testing and 20 percent for training.  The training dataset is used for what we saw previously tweak the algorithm such that it minimizes error or some other metric.  Then, now that the algorithm is optimized, they see how well their algorithm performs on something it is not molded to, called test data.  If the algorithm performs well on the test data, then it is ready to use to make new predictions.

#### All together

So these four concepts are all related.  Underfitting occurs when our algorithm is not responsive enough to our data, and therefore we can optimize our algorithm to better predict our existing data.  Changing our algorithm such that it responds to our data is called **training**.  The risk of training the algorithm to an existing data set is that the algorithm can pick up on the quirks of the data, such that it will not generalize to new data.  This is called **overfitting**.  To prevent against overfitting, data scientists set aside a portion of the data that they are not training their algorithm with.  Seeing if their algorithm properly predicts this new data as well is called **testing**. 

### Summary

So as you can see, there is a very structured approach, and a lot of thought that can go into just choosing the correct k size.  At this point, we do not need to be so formal when choosing our k size.  As we'll see in the next section, by choosing a correct k, we can still derive a nearest neighbors algorithm that is fairly predictive of our data.

In this lesson, we reviewed the nearest neighbors function and saw how it derives from calculating the distance using the Pythagorean Theorem to then sorting neighbors by that interest.  



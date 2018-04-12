
# Applying Nearest Neighbors 

### Introduction

In the last lesson we derived the nearest neighbor formula.  Nearest neighbors is a powerful algorithm because it allows us to predict other attributes about people using their proximity data.  For example, those who live in a particular neighborhood may be more likely to be a certain age or have similar interests.  Using proximity, we might even be able to determine whether their likelihood to purchase a product approximates that of their neighbors.

In this lesson we'll see how the nearest neighbors algorithm allows us to make predictions with data.  We will also look at the workflow for machine learning in general and see some of the common struggles that we experience when applying a machine learning algorithm. 

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

We represent these individuals along with their yearly purchases in Python with the following:


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

Just by looking at this data, aside from Suzie, it seems that the proximity of customers provides a good indication of the number of cupcake purchases per customer.  Assume that a new customer just purchased his first cupcake, and we want to develop some expectation for how many cupcakes he may purchase from us in the following year.  His location may help us determine the ingredients we need to buy to satisfy his demand.  Let's see what the nearest neighbors algorithm tells us.

### Apply our nearest neighbors algorithm

Here is the nearest neighbors algorithm once again.  The code below reflects the following steps:

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

We try our `nearest_neighbors` function on a known piece of data, `bob`.  When we ask our function to return only the closest neighbor, it returns Fred and tells us his number of purchases.  Perhaps we can expect Bob's number of purchases to be similar to Fred's.  We also can apply the function to a customer at new location to predict this customer's number of purchases.


```python
nearest_neighbor_to_new = nearest_neighbors({'x': 4, 'y': 3}, neighbors, 1)
nearest_neighbor_to_new
```

However, simply choosing the **nearest neighbor** seems like an arbitrary way to estimate number of purchases.  Our estimate is determined by just one individual's purchases.  We ought to expand the number of neighbors and take the average of their purchases to produce a better estimate for purchases by someone at this new location.


```python
nearest_three_neighbors = nearest_neighbors({'x': 4, 'y': 3}, neighbors, 3)
nearest_three_neighbors
```


```python
purchases = list(map(lambda neighbor: neighbor['purchases'],nearest_three_neighbors))
average = sum(purchases)/len(purchases)
average # 43.0
```

### Choosing the number of neighbors

In the above section, we use the nearest neighbors formula to make a prediction.  It's telling us that someone who lives on 4th street and 3rd Avenue is expected to purchase 45 cupcakes.  This approach is highly flawed since our algorithm's predictions change dramatically depending upon the number of neighbors we include in our formula.  The number of neighbors that we choose in the nearest neighbors algorithm is represented by `k`.

Choosing the correct number of neighbors to consider touches upon a number of themes in data science.  We'll introduce a few of these issues here, so we are aware of them as we visit other machine learning problems.

#### Underfitting

**Underfitting** occurs when our formula does not pick up on the relevant signals from the data.  For example, if the number of neighbors we have is too large, our algorithm would improperly predict the purchases of our known customers, as it would fail to respond to differences in location.

#### Minimizing for error

How do we determine the correct number for `k`, the number of neighbors to consider?  One way is to see how well our algorithm predicts against our existing data, then make the necessary changes.

For instance, when we look at Bob's closest neighbor by setting `k = 1`, the nearest neighbor algorithm expects Bob to make 60 purchases. We already know that Bob actually purchased 52 cupcakes, so our formula is off by 8.  This number, our actual value minus the expected value, is called the **error**.  We can optimize the algorithm by adding all of the errors across all of the neighbors and selecting that `k` which minimizes this aggregate error for all of our data.

#### Training 

This approach of looking at our existing dataset to optimize for some metric, like the lowest error, is called **training**. In this example, we train our algorithm by choosing numbers of `k` such that our algorithm optimizes for predicting the number of purchases in our dataset.

#### Overfitting

However, when training our algorithm to match our data, **overfitting** could become a problem.  Overfitting occurs when we overgeneralize from the data.  If we are served a bad meal at a chain restaurant, we could improperly conclude that all meals at the chain are bad.  The same thing can happen with our algorithm.

Our algorithm can be optimized for and perform well with our existing data, but not do well with new data.  Imagine that we have one hundred cupcake customers and choosing a `k` of 2 best minimizes the error in predicting the number of purchases.  We could find later that, as we get new customers, our model does not predict their purchases.

The algorithm could pick up on things particular to our existing data set, but fails to generalize to new data.

#### Testing 

To see whether the algorithm fits new data, we should test it with new data.  Data scientists cannot waste time waiting for new data to arrive, so they split their data in two: roughly 80 percent of the data for testing and 20 percent for training.  The training dataset is used for tweaking the algorithm, as we just saw, so that it minimizes the error or some other metric.  Once the algorithm is optimized, they study how well their algorithm performs on something it is not molded to, called test data.  If the algorithm performs well on this test data, it is ready for use and can make new predictions.

#### All together

So these four concepts are all related.  Underfitting occurs when our algorithm is not responsive enough to our data, and therefore we can optimize our algorithm to better predict our existing data.  Changing our algorithm so it responds to our data is called **training**.  **Overfitting** is the risk of training the algorithm to an existing data set to the extent that it picks up on the quirks of the data and fails to generalize to new data.  To prevent against overfitting, data scientists set aside a portion of the data for **testing** to determine if the algorithm properly can predict on this portion of the data. 

### Summary

In this lesson, we reviewed how to collect and explore data by implementing the Pythagorean Theorem and the sorting method to build our nearest neighbors algorithm.  We then learned how we could train the algorithm so that it can produce predictions about incoming data.


As you can see, there is a very structured approach, and a lot of thought that goes into simply choosing the correct `k` size.  At this point, we need not be so formal when choosing our `k` value.  We'll learn in the next section that by choosing a correct `k`, we still can derive a nearest neighbors algorithm that is fairly predictive of our data.

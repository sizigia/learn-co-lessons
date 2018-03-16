
# Nearest Neighbors

###  Learning Objectives

* Understand how to use the Pythagorean Theorem to build a nearest neighbors function

### Writing a nearest neighbors function

Previously, we used the Pythagorean Theorem to calculate distances between individuals.  In the last lab we used this to write a nearest neighbors function to return a list of the closest neighbors to a given individual.  Let's review that now.

Once again, here were the locations of Bob and our customers:

| Name | Avenue #| Block # | 
|------|------| ------     |
| Bob    | 4  |     8     | 
| Suzie  | 1  |     11     | 
| Fred   | 5  |     8     | 
| Edgar  | 6  |     13     | 
| Steven | 3  |     6     | 
| Natalie| 5  |     4     | 

And we represent these individuals in Python with the following:


```python
neighbors = [{'name': 'Bob', 'x': 4, 'y': 8}, {'name': 'Suzie', 'x': 1, 'y': 11}, 
             {'name': 'Fred', 'x': 5, 'y': 8}, {'name': 'Edgar', 'x': 6, 'y': 13},
             {'name': 'Steven', 'x': 3, 'y': 6}, {'name': 'Natalie', 'x': 5, 'y': 4}]
bob = neighbors[0]
suzie = neighbors[1]
```

To write a `nearest_neighbors` function, we break this into steps:

1. Write a function to calculate the distance of one neighbor from another
2. Write a function that returns the distance between one neighbor and all others (using `map`)
3. Return a selected number of nearest neighbors

### Calculating the distance of one neighbor from another

**First**, we write a function that calculates the distance between one individual and another.  This function is a translation of our Pythagorean Theorem, which says that given a first individual with coordinates $(x_{1}, y_{1})$, and a second individual with coordinates $(x_{2}, y_{2})$, then $distance = \sqrt{(x_{2} - x_{1})^2 + (y_{2} - y_{1})^2}$.


```python
import math

def distance(selected_individual, neighbor):
   distance_squared = (neighbor['x'] - selected_individual['x'])**2 + (neighbor['y'] - selected_individual['y'])**2
   return math.sqrt(distance_squared)
```


```python
def distance_between_neighbors(selected_individual, neighbor):
    neighbor_with_distance = neighbor.copy()
    neighbor_with_distance['distance'] = distance(selected_individual, neighbor)
    return neighbor_with_distance
```


```python
distance_between_neighbors(bob, suzie)
```




    {'distance': 4.242640687119285, 'name': 'Suzie', 'x': 1, 'y': 11}



The `distance_between_neighbors` function makes a copy of the neighbor object and then adds a new attribute called distance using the previous `distance` function. So now we have associated a neighbor with his/her distance from a given point.

### Creating a list of neighbors with distances

**Next**, we write a `distance_all` function to calculate the distance between a `selected_individual`, and all of the other neighbors.  We do this by calling our `distance_between_neighbors` function with the `selected_individual` and each of the rest of the neighbors.

In the `distance_all` function, we first filter out the `selected_individual` as we don't want to return the selected individual as a neighbor.  Then we  calculate the distance between the `selected_individual` and the rest of the individuals.  Finally, for each of the remaining neighbors, we use our `distance_between_neighbors` method to add in a distance attribute to each of the neighbors.


```python
def distance_all(selected_individual, neighbors):
    remaining_neighbors = filter(lambda neighbor: neighbor != selected_individual, neighbors)
    return list(map(lambda neighbor: distance_between_neighbors(selected_individual, neighbor), remaining_neighbors))
```

### Return selected number of nearest neighbors

Finally, we write our `nearest_neighbors` function.  The function takes an optional argument of `number`, which represents the number of "nearest" neighbors to return.  When set to `None`, `number` is reassigned to equal the length of the `neighbors` list.  The `nearest_neighbors` function finishes by sorting the the "neighbors" by their distance and then slicing the list to return the correct number of neighbors.     


```python
def nearest_neighbors(selected_individual, neighbors, number = None):
    number = number or len(neighbors)
    neighbor_distances = distance_all(selected_individual, neighbors)
    sorted_neighbors = sorted(neighbor_distances, key=lambda neighbor: neighbor['distance'])
    return sorted_neighbors[:number]
```


```python
nearest_neighbors(bob, neighbors)
```


```python
nearest_neighbors(bob, neighbors, 2)
```

### Summary

In this lesson, we reviewed the nearest neighbors function and saw how it derives from calculating the distance using the Pythagorean Theorem to then sorting neighbors by that interest.  



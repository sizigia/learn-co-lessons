
# Multivariable Functions

* Understand how multivariable function can be represented as a 3d graph
* Understand how, when we think of the error, or cost of a regression function it varies with changing slope and y-intercept values
* Understand how to think about the a regression line's cost curve in three dimensions

### Reviewing where we've been and why we're here 

Ok, so before moving on, let's pull back a little bit and make sure we understand where we are.  Remember, that we started this discussion by simply plotting our data.  Then we moved to drawing a regression line to estimate how a change in our input affects a change in our output.

![regression-scatter.png](attachment:regression-scatter.png)

Now, because our regression lines do not perfectly predict our data, we put a number to a regression line's accuracy by calculating the residual sum of squares (RSS).  And as we know, the size of the RSS is a function of our y-intercept and slope values, and we can plot our RSS as a function of one of these variables.

![](./cost-curve.png)

Because we want to approach our best fit line in an efficient manner, we can use look to the slope of our cost curve at the value of a y-intercept to tell us whether to increase or decrease our y-intercept variable and how large of a step to update it.   We imagined standing on our two dimensional cost function, and even without knowing what the rest of our cost function looks like, using the slope to point us towards our minimum and taking a step towards the minimum proportional to the magnitude of the slope.  This technique is called gradient descent.  To talk about how to calculate slopes of line, we got into a discussion of derivatives.  There we learned how to think about them conceptually, as well as rules for calculating derivatives. 

![](./tangent-lines.png)

Now so far this entire context, from modeling a cost curve, to moving along that cost curve by a distance proportional to the slope, to calculating the slope, has just been in the context of changing a single variable of our regression formula $y = mx + b $.  We've only asked how our cost curve changes as we alter a variable like $b$.

### Going further

But in our regression line of $y = mx + b $ it is not just the y-intercept $b$ we are changing to minimize our error, but the slope of the line, $m$, as well.  So this means that our error is a function of both variables, the y-intercept and the slope.

![](./regression-scatter.png)

As we shift our line up or down by changing the y-intercept, the error changes.  In addition, as we change the slope of the function the error changes.  So now, thinking about our cost curve, it is really not a two dimensional curve that we are walking along, but a three dimensional one.

![gradientdescent.png](attachment:gradientdescent.png)

Let's spend some time looking at this curve.  What we are expressing is that unlike in the past, we don't just need to shift a value of our y-intercept and keep our slope constant, but can change both variables.  As we change our regression line's slope and y-intercept, the cost of the function changes.  Before we talk about doing anything with a 3-d cost curve, let's just make sure we understand how to think about 3-d graphs and multivariable functions.

### Thinking in multivariables

Ok, so let's talk multivariable functions in general.  With a multivariable our output is no longer a function of just one variable, so we cannot use $f(x)$ or $f(y)$ to describe our function.  Instead, as you know, with an output varying based on two inputs, we express this with $f(x, y)$.  

Ok, now let's take a look at a real, live multi-variable function:

$$ f(x,y) = y* x^2 $$

This is what the function $f(x, y) = y*x^2 $ looks like:

![](./parabolayx2.png)

It takes a minute to see it, but this three dimensional graph of $f(x,y) = y*x^2$ makes sense.  Here's why.  Let's remember that the function $f(x) = x^2$ looks just like a smiley face.  Mathematicians call the smiley face a parabola.

<img src="./parabola.png" alt="Drawing" style="width: 300px;"/> 

Our parabola reflects our function squaring it's output for every input.  So for the function, $f(x)$ = x^2$, $f(2) = 4 $ and $f(3) = 9 $.

Now our function $f(x, y) = y*x^2 $ means that this parabola is multiplied by the value of $y$.  So that when $y = 2$, for example, $f(x, 2) = 2x^2 $ the parabola is twice as steep as each output doubles.  And a negative $y$ in the function $f(x,y) = y*x^2$  flips our parabola upside down.  Take a second to consider what the graph looks like at different values of $y$.

Take a look one by one of the graphs below, which display what happens as we step through different values of $y$.  The parabola is flipped for a negative $y$.  And the further $y$ moves away from zero the steeper the parabola.  

![](./yx2-frames.png)

You can almost think of the graphs above as different freeze frames of our three dimensional function.  And looking at the three dimensional version by guiding your from negative $y$ values to positive $y$ values is having a movie take us through these frames in a cohesive viewing experience. 

![](./parabolayx2.png)

So now that we are reoriented, does it make more sense why the graph above maps to the function $f(x,y) = y*x^2$?  Do you start to see how and why the output of our function changes as the values of $y$ change?  And as the values of $x$ change?  Feel free to re-read this section to let it sink in.

### Moving back to our cost function

So now that we understand how to think about three dimensional graphs a little bit more, let's go back to thinking about our regression lines.  Do you begin to see how the graph displays how changing the slope of the line and changing the y-intercept of the line returns a different output of our cost function?

![](./gradientdescent.png)

Now think about our regression line again, displayed below.  Think about how changing the y-intercept or changing the slope of our regression line relates to a move along our 3-d graph and a change in our cost function's output. 

![](./regression-scatter.png)

If you feel comfortable with that, give yourself a pat on the back.

### Summary 

In this section, we started thinking about the cost related to a dimension line not only as a y-intercept changes, but also as the slope changes.  To do this, we talked about multivariable functions in general, and how one can even think of of a three dimensional graphs in terms of successive two dimensional graphs.  This is how we can think of our cost curve, as matter of shifting one or both of the variables of our regression line, and seeing the resulting change to the function's accuracy.   

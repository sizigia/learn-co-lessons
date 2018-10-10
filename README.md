
### Introduction

![](./tree.jpg)

Before moving on, let's take a step back.

In the supervised learning algorithms that we have looked at so far, we are chugging along by following our process.

* **Collect**: Gather and clean the relevant data
* **Explore**: Explore the data
* **Train**: Choose a statistical or machine learning model (ie. a tool or algorithm) and optimize the model for some criteria (eg. how well the model predicts our data)
* **Predict**: Make predictions with the trained model

As we mentioned, for collecting and exploring the data we mainly use our Python skills and knowledge about the domain.  Training a model is more about machine learning.  

In linear regression analysis, our model is a regression line.  We use it to **model** the real world relationship between our explanatory variable and our dependent variable.  How do we know what that *real world relationship* is?  Because this is supervised learning, it comes from our existing *actual* data.  So, in the example we've been using, the actual data we have is the revenue, and we train our model by developing a regression line that minimizes the difference between the actual data and what our model expects.  

### Training a model

This training step is where calculus comes in.  By training a model, we move along a loss function, and calculus can tells us where to move next to work towards minimizing this loss function.



So training a model, and loss functions, and calculus, don't just come into play with regression lines.  Many algorithms in machine learning have a loss function, such that as we change the parameters of a model, the cost associated with that model changes.  Calculus can gives us an expectation as to how the cost associated with a model changes as we update that model.  In general, calculus can tell us *the rate of change*, and if we know how our cost function is changing, we can use this knowledge about how our loss changes as we change a parameter, to tell us how to change a parameter next.

Already we have seen this by looking at the slope of the line to our cost function to see how to update our regression line.  That slope tells us how much our cost is changing as we change a single parameter of our model, and indicates how to change that parameter to improve our cost.

Now as our models become more complex and there are more levers to pull, having a technique that tells us how to change the model next becomes very powerful.

### Summary

So in summary:
* We'll use other types of models beyond drawing a regression line.  
* However, there will be loss functions.  
* And we will want adapt our model so that it begins to minimize the output from our loss function.  
* That is training our model.  
* And calculus can tell us how to update our machine learning model and the change in output that will occur as a result 

So moving along that loss function to approach the minimum in a structured way requires math, and derivatives.  

The sections that follow will take a deep dive into mathematics and that will underly our future machine learning techniques.  Taking this exploration will allow us to understand our current machine learning model of gradient descent, as well how we can train other machine learning models in the future.

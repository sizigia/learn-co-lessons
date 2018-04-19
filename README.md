
### Introduction

![](./tree.jpg)

Before moving on, let's take a step back.

In the supervised learning algorithms that we have looked at so far, we are following a consistent process.

* **Collect**: Gather and clean the relevant data
* **Explore**: Explore the data
* **Train**: Choose a statistical or machine learning model (ie. a tool or algorithm) and optimize the model for some criteria (eg. how well the model predicts our data)
* **Predict**: Make predictions with the trained model

As we mentioned, for collecting and exploring the data we mainly use our Python skills and knowledge about the domain.  Training a model is more about machine learning.

### Training a model

Our model is our regression line.  We use it to **model** the real world relationship between variables.  How do we know what that *real world relationship* is?  Because this is supervised learning, it comes from our existing *actual* data.  So, in the example we've been using, the actual data we have is the revenue, and we train our model by developing a regression line that minimizes the difference between the actual data and what our model expects.  

As we go to learn more machine learning techniques: 
* we'll use other types of models beyond drawing a regression line.  
* And we'll use other types of loss functions beyond our Residual Sum of Squares like we have been using.  
* However, there will be loss functions.  

And we will want adapt our model so that it begins to minimize the output from our loss function.  That is training our model.  

And moving along that loss function to approach the minimum in a structured way requires math, and derivatives.  

The sections that follow will take a deep dive into mathematics and that will underly our future machine learning techniques.  Taking this exploration will allow us to understand our current machine learning model of gradient descent, as well how we can train other machine learning models in the future.

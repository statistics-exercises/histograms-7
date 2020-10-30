# Calculating the histogram

Now that you can sample from a multinomial distribution we are in a position to introduce the key idea that I wanted to get to in this series of exercise; namely, the process  of estimating the probability mass function for a random variable by calculating a histogram.  This is the idea that we are going to work on in this exercise.  Furthermore, the code that you are going to write is going to be very similar to the code that you wrote for generating samples from the multinomial distribution.  Now, however, the final output will not be a list of random variables.  The code in the box on the left will instead output a bar chart showing the histogram that you obtained by sampling the distribution.  

To complete this code you will need to:

1. Write a function called `myvariable` that takes a list of probabilities called `probs` as input and that generates a discrete random variable from a distribution  the  probability mass that follows this list
2. Call the function `myvariable` in order to generate 200 samples from this distribution.  Use the array called `counts` to count how often each of the various possible values this random variable can take comes up in these samples.  As always you do not need to use if statements to do this counting as you can use the value of the random variable to refer to the appropriate element of the list.  
3. Convert the `counts` of how often each variable comes up to a fraction that measures the fraction of samples for which the random variable was equal to each of the possible value for the random variable.

If you have completed the code correctly the heights of the bars in the chart that will appear should be similar to the probabilities in the probability mass function below:

![](https://render.githubusercontent.com/render/math?math=P(X=0)=0.5\qquad\P(X=1)=0.1\qquad\P(X=2)=0.2\qquad\P(X=3)=0.05\qquad\P(X=4)=0.15)

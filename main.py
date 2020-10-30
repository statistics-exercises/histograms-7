import matplotlib.pyplot as plt
import numpy as np

def myvariable( probs ) : 
  # Your code to generate a random variable from the distribution that 
  # has been given in the instructions goes here
  
  
probs, counts = np.array([0.5, 0.1, 0.2, 0.05, 0.15 ]), np.zeros(5)
for i in range(200) : 
  # Your code to generate multiple random variables using the function
  # called myvariable above and to count how often each outcome comes
  # up goes here.
  
  

for i in range(5) : 
  # Your function to convert the count of the number of times each 
  # value for the random variable comes up to the fraction of times
  # each outcome comes up goes here.
  
  
  
# These command will plot your histogram
plt.bar( [0,1,2,3,4], counts, width=0.1 )
plt.xlabel("Random variable value")
plt.ylabel("Fraction of occurances")
plt.savefig("myhistogram.png")

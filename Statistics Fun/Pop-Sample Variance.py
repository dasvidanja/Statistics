''' The dilemma of Variance is it N  (pop size) or n-1 (n samp size)

Population Var: sum((x-mu)^2) / N
Sample Var: sum((x-mu)^2) / n-1

The idea is that if we divide by N when we have a sample we will get a biased estimate
of the Variance (it will be underestimated, especially for small size samples). 

Hence to correct for this underestimation, given that almost always we are dealing with 
a sample from a population with unknown Variance, it has been proven that we will get 
the true variance given we divide by n-1 instead of n.

**Proof (TO BE DONE)

'''

#Experiment 1.10 
import numpy as np
from scipy import stats

#Generate 1000 random numbers from a population (i.e # 0-9)
random_num = list()
for x in range(1000):
    random_num.append(np.random.randint(0,10))
    
#Find variance of this population
N = len(random_num)
pop_mean = np.mean(random_num)
residuals = sum((random_num-pop_mean)**2)
pop_var = residuals/N 
print("Population variance: ", pop_var)

#Repeatedly take resamples of size 10 and calculate the variance for each resample 
#accordingto the same population formula. 
sample_variance = list()
y=0
z=9 
#There are 100 -10 samples in 1000
for x in range(100):
    #10 elemetns
    temp = random_num[y:z]
    #Calculate variance as if population
    N_s = 10
    pop_mean_s = np.mean(temp)
    residuals_s = sum((temp-pop_mean_s)**2)
    pop_var_s = residuals_s/N_s
    sample_variance.append(pop_var_s)
    y=z+1
    z= z+10


#How does the mean of the resample variances compareto the population variance?
print("Mean: ", np.mean(sample_variance))

'''The variance has been underestimation.''


''' Result year one 7 major mistakes
           year two 3 major mistakes,
    Question was this due to chance, or was this due to the new policy that was put in place?
    
Head= first year, Tails= second year

Perform a test where we can check if 7 heads is indeed a plausible event or weather this is a very unlikely event.'''
import numpy as np 

def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success, a.k.a HEADS
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number<p:
            n_success +=1

    return n_success
    
# Seed random number generator
#np.random.seed(43)

#From each Experiment of 12 trials with 10 outcomes in each trial get probability >=7
def trial_outcome():
    # Initialize the number of defaults: n_defaults
    n_defaults = np.empty(12)

    # Compute the number of defaults
    for i in range(12):
        n_defaults[i] = perform_bernoulli_trials(10,0.5)
        
    event_of_7_heads = sum(n_defaults>=7)
    
    #probability
    probability= event_of_7_heads/12
    
    #The probability of seeing a result as extreme as the observed value (the famous p-value)
    return probability

#Determine the stability of the result by repeating the experiment 1000 times
total_pro = []    
for x in range(1000):
    total_pro.append(trial_outcome())
    

#Plot
import matplotlib.pyplot as plt

n_data = len(total_pro)
_= plt.hist(total_pro, bins= int(np.sqrt(n_data)) )   

#Looks like this is the theoretical mean  (a.k.a E[X]) :)     
print(2/12)

    
    
    
    
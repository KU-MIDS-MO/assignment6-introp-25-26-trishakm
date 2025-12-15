import numpy as np
def estimate_pi(num_samples):
    
    
    for i in range(1000):
        x = np.random.rand(num_samples)
        y = np.random.rand(num_samples)
        
        in_circle = (x*x + y*y) <= 1
        
            
    pi = 4 * np.mean(in_circle)
    
    return pi
        
    pass

num_samples = 1000
print(estimate_pi(num_samples))


#Write a function:
#`estimate_pi(num_samples)`
#that:
#returns an estimate of π using num_samples random points generated with np.random.rand().
import numpy as np
from scipy.special import gamma

def t_distribution_pdf(x, nu):
    coeff = gamma((nu+1)/2) / (np.sqrt(nu*np.pi)*gamma(nu/2))
    density = coeff*(1+x**2/nu)**(-0.5*(nu+1))
    return density

def find_t_star(prob, nu, x_start=0, x_end=20, num_points=10000):
    x = np.linspace(x_start, x_end, num_points)
    y = t_distribution_pdf(x, nu)
    cdf = np.cumsum(y) * (x[1] - x[0])
    target_half_prob = prob / 2
    index = np.where(cdf >= target_half_prob)[0][0]
    return x[index]


list = [92.64,79.00,84.79,97.41,93.68,65.23,84.50,73.49,73.97,79.11]
mean = np.mean(list)
stddev = (np.sqrt(np.sum((list - mean)**2) / (len(list) -1 ))) / np.sqrt(len(list))
print(mean)
print(stddev)

tstar = find_t_star(0.95, len(list)-1)
tnaught = ((mean - 75)/stddev) #alr accounts for sqrt of n

def ttest():
    if np.abs(tnaught) > tstar:
        return False
    else:
        return True
print("The mean I got was", mean)
if not ttest():
    if tnaught > tstar:
        print("Test scores are higher, based on the mean")
    elif tnaught < tstar:
        print("The test scores are lower, based on the mean")




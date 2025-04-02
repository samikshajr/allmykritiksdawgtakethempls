import numpy as np
import matplotlib.pyplot as plt

def norm_den(mean, variance, x):
  J = ((np.exp((-((x-mean)**2))/2*variance))/np.sqrt(2*np.pi*variance))
  return J

def integration(mean, variance, a,b):
  n = 1000
  x = np.linspace(a,b,n+1)
  dx = (b-a)/n
  probability = 0
  for i in range(n):
    probability += dx*norm_den(mean, variance, x[i])
  return probability


mnot = 0
vnot = 1
x1 = np.linspace(mnot - 10 * vnot, mnot + 10 * vnot, 10000)
y1 = []
for i in range(10000):
  y1.append(norm_den(mnot, vnot, x1[i]))


plt.plot(x1, y1)
plt.grid()
plt.xlim(-10, 10)
plt.ylim(0,0.5)
plt.show()

mean2 = 171
variance2 = 7.1
x2 = np.linspace(mean2 - 4 * variance2, mean2 + 4 * variance2, 10000)
y2 = []
for i in range(10000):
    y2.append(norm_den(mean2, variance2, x2[i]))

plt.plot(x2, y2)
plt.xlim(mean2 - 10 * variance2, mean2 + 10 * variance2)  # define limits for x-axis
plt.ylim(0, 0.2)  # define limits for y-axis
plt.grid()
plt.show()

print("Probability for a randomly chosen guy to have a height between 162cm and 190cm is " + str(
    integration(mean2, variance2, 162, 190) * 100) + "%.")


#a
def uniform_distribution_expected(a, b):
    n = 1000000
    x = np.linspace(a, b, n + 1)
    delta_x = (b - a) / n
    integ = 0
    for i in range(n):
        integ += x[i] * (1 / (b - a)) * delta_x

    return integ


print(str(uniform_distribution_expected(1, 100)))

#b
def exponential_distribution_expected(rate):
    n = 1000000
    a = 0
    b = 1000000
    x = np.linspace(a, b, n + 1)
    delta_x = (b - a) / n
    integ = 0
    antiderivative = 0
    for i in range(n):
        integ += x[i] * (rate * np.exp(-rate * x[i])) * delta_x

    antiderivative = (-b*np.exp(-rate * b)-np.exp(-rate * b)/rate)-((-a*np.exp(-rate * a)-np.exp(-rate * a)/rate))
    # print(antiderivative)
    return integ

print(str(exponential_distribution_expected(1 / 50)))
print("Yes, this is what's to be expected in 50 yers based on the definite integral using experimental data and the antider.")

#c
def normal_distribution(mean, variance, x):
  return (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-(x - mean) ** 2 / (2 * variance))


def normal_distribution_expected(mean, variance):
  n = 100000
  a = mean - 4 * np.sqrt(variance)
  b = mean + 4 * np.sqrt(variance)
  x = np.linspace(a, b, n + 1)
  delta_x = (b - a) / n
  integ = 0
  for i in range(n):
    integ += (2.38*(171**2)/norm_den(mean, variance, x[i]) * delta_x)
  return integ

avg_dose = normal_distribution_expected(171, 7.1)

print(avg_dose)

print(2.38 * (171 ** 2))
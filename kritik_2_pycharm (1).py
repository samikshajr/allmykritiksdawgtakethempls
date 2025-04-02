import numpy as np
# use def to set roots
def roots(f, a, b, tol = 1e-10): #tol means 'tolerance' - I've used it to specify 10 decimal places here
    if f(a)*f(b) >= 0:
        print("Both endpoints are positive: they have the same sign. Please try again!")

    while (b-a) / 2 > tol: #one interval is the distance b/w a and b. Since we are using the bisection method, we divide each interval by two every time. The difference should be higher than 1e-10
        midpoint = (a+b) / 2
        if f(midpoint) == 0: #solution has been found
            print (midpoint)
        elif f(a) * f(midpoint) < 0: #the solution is in the left half of the interval --> [(a+b)/ 2, b]
            b = midpoint
        else:
            a = midpoint #solution is in the right half of interval -->[a, (a+b)/2]
    return midpoint

#test functions are listed below. They have been defined as functions. Make sure to check syntax!
def test_f1(x):
    return np.exp(x) + np.log(x)  # f(x) = e^x + ln(x)

def test_f2(x):
    return np.arctan(x) - x**2  # f(x) = arctan(x) - x^2

def test_f3(x):
    return np.sin(x) - np.log(x)  # f(x) = sin(x) - ln(x)

def test_f4(x):
    return np.log(np.cos(x))  # f(x) = ln(cos(x))

#now we must make sure to try out the biesction method with the test functions
print("The solution of f(x) = e^x + ln(x) on [0, 1] is ", roots(test_f1, 0, 1))
print("The solution of f(x) = arctan(x) - x^2 on [0, 2] is ", roots(test_f2, 0, 2))
print("The solution of f(x) = sin(x) - ln(x) on [3, 4] is ", roots(test_f3, 3, 4))
print("The solution of f(x) = ln(cos(x)) on [5, 7] is ", roots(test_f4, 5, 7))
print("Testing complete. Try again with new points!")
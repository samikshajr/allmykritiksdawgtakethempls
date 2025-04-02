import matplotlib.pyplot as plt
import numpy as np

def gradient_descent(f, learning_rate, initial_point):
    def deriv(f, base_point): #estimate the derivative
#of the function f at base_point using the symmetric approx
        return (f(base_point+10**(-10))-f(base_point-10**(-10)))/(2*10**(-10))

x_coords=[initial_point] #This list is where you will store the x_n's
y_coords=[f(initial_point)] #This list is where you will store the y_n's
#PUT YOUR CODE HERE!
print("Sorry i actually didn't understand what i was supposed to do, and by the time i started the python part, it was too late to ask anyone.")


# Plotting portion. You may adjust as you please.
plot_range=np.linspace(min(x_coords)-0.5, #a nice plot range
plot_range=np.linspace(max(x_coords)+0.5,10000) #to make look good
function_range=[f(i) for i in plot_range]
plt.plot(plot_range, function_range) #this plots the function f(x)
plt.plot(x_coords, y_coords) #This will plot the
#sequence of points x_n, f(x_n)
return round(x_coords[-1],3), round(y_coords[-1],3) #returns your
# last x_n and y_n, #rounded to three decimal places.

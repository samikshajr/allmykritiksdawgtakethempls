#Kritik q4
x = float(input("Please type in a number here:"))

def all_encompassing(x):
    if x < 0 or x > 1:
        return "Error! Pick a number between and including 0 and 1 instead..." #this is outside the range of values stated in the question

    elif x>=0 or x<=1: #if input is within range
        def error(a,b): #error function
            y = (a**((2*b)+1)) / ((2*b)+1) #a^2b+1 / 2b+1
            return y

        n=0
        while error(x,n) > 0.0001: #can be run as long as the error is 0.0001 or less
            n+=1

        changing = 0
        for i in range(n):
            original = (((-1)**i)*(x**((2*i)+1))) / ((2*i)+1)
            changing += original

    return (changing,n,error(x,n))
print(all_encompassing(x))

lower = int(input("Enter lower range limit"))
upper = int(input("Enter upper range limit"))
for i in range(lower, upper+1):
    if(i%3==0) & (i%5==0):
        print("fizzbuzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else:print("Not in range")
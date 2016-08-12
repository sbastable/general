#!/usr/bin/python3

# Function definition is here
def printme(a,b,c):
   "This gives values of x where ax^2+bx+c = 0"
   #"(-b +/- sqrt(b^2-4ac))/2a"
   xresultone = (-b + (b**2 - (4 * a * c))**(0.5)) / (2 * a)
   xresulttwo = (-b - (b**2 - (4 * a * c))**(0.5)) / (2 * a)
   print (xresultone,end=";")
   print (xresulttwo)
   return

# Now you can call printme function
printme(a=1,b=5,c=4)

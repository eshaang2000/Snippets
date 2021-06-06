def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
  
a = 296222421959119451995996652753
b = 238018309085661228954182465677
  
# prints 12 
# print ("The gcd of 60 and 48 is : ",end="") 
print (computeGCD(a, b)) 

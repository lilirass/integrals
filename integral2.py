#midpoint rule
def integral(a,b,npoints):
   
   dx=(b-a)/(npoints)
   def f(x):
      return x**3
   value=0
   n=1
   while n <=(npoints):
      xpoint= a +((2*n-1)/2)*(dx)
      value += f(xpoint)*(dx)
      n +=1
   return value

res= integral(0,1,4)
print (res)
res= integral(1,3,4)
print (res)
res= integral(1,3,100)
print (res)

def precision(a,b,npoints,p):
   n=npoints
   m= 2*npoints
   A=integral(a,b,n)
   B=integral(a,b,m)
   p_value = float(abs(A-B))
   if p_value <= p:
      result="good accuracy"
      
   elif p_value > p:
      while p_value > p:
         m=m+m
         n=n+n
         A=integral(a,b,n)
         B=integral(a,b,m)
         p_value=float(abs(A-B))
         print(p_value,m)    
      result= "the ideal npoints is",n
   return result

print(precision(1,3,5,0.02))
print(precision(1,3,10,0.0002))

 
      
   

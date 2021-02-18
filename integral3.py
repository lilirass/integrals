def integral(a,b,npoints):
#Simpson rule integral=(dx/3)[f(a)+2f(i=even)+4f(i=odd)+f(b)] 
    dx=(b-a)/(npoints)
    #define the function f(x), it can be any function
    def f(x):
       return x**3
    #B=sumf(i=odd) and C=sumf(i=even)
    B=0
    C=0
    i=1
    while i < npoints:
        if i%2 !=0 :
            B=B+f(a+i*(dx))
            i=i+1
        elif i%2 ==0:
            C=C+f(a+i*(dx))
            i=i+1
    result = ((dx)/3)*(f(a)+4*B+2*C+f(b))
    return result


answer= integral(2,10,5)
print (answer)
answer= integral(2,10,10)
print (answer)
answer= integral(1,3,100)
print (answer)


#precision function
def precision(a,b,npoints,p):
    n=npoints
    m= 2*npoints
    A=integral(a,b,n)
    B=integral(a,b,m)
    p_value=float(abs(A-B))
    #print("p_value is:",p_value)
    #print ("A is :",A)
    #print("B is:",B)
    if p_value <= p:
        res="good accuracy"
      
    elif p_value > p:
        while p_value > p:
            m=m+m
            n=n+n
            A=integral(a,b,n)
            B=integral(a,b,m)
            #print(B)
            p_value=float(abs(A-B))
            print(p_value,n)    
        res= "the ideal npoints is:",n
    return res

print(precision(1,3,5,0.02))
print(precision(1,3,10,0.002))
print(precision(3,4,2,0.01))

 
      
 

#1`
s=input("Enter a string: ")
l=len(s)
s2=''
for i in range(l-1,-1,-1):
            s2=s2+s[i]
print("Reversed string is", s2)

#2
x1,x2=input("Enter the range of numbers: ").split()
x1=int(x1)
x2=int(x2)
n= int(input("Enter number: "))
for i in range(x1,x2,1):
    if i%n==0:
        print(i)
        continue
import math
a=int(input("Enter first side of triangle: "))
b=int(input("Enter second side of triangle: "))
c=int(input("Enter third side of triangle: "))
if a<0 or b<0 or c<0:
    print("Invalid input, side cannot be negative")
elif(a+b<c or b+c<a or c+b<a):
    print("Combination of sides is not possible")
else:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Area of the triangle is {area}")
    print()
    
#4
rows=5
for i in range(0,rows):
    for j in range(0,i+1):
        print("* ",end='')
    print()
    
#5
rows=int(input("Enter the number of rows: "))
x1=int(x1)
x2=int(x2)
for i in range(x1,x2,1):
    c=0
    n=1
    while n<=i:
        if i %n==0:
            c+=1
            n+=1
            continue
        n=n+1
    if c==2:
        print(i)
print()

#6
for i in range(1,500):
    if i%7==0 and i%11==0:
        print(i)
print()

#7
for i in range(0,10,1):
    n=int(input(f"Enter {i+1}th number: "))
    list.append(n)
print(list)
               
#8
str=input("Enter a string: ")
counts=dict()
words=str.split(' ')
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word] = 1
print(counts)
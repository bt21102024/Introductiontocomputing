#1
def perfect_number(n):
   s=0
   for i in range(1,n):
       if(n%i==0):
           s+=i
   if(s==n):
       return True
   else:
       return False
   
N=int(input("Enter a number: "))
if(perfect_number(N)==True):
    print(N, "is a perfect number")
else:
    print(N, "is not a perfect number")
print()

#2
def palindrome(s):
    s1=""
    s1=s[s::-1]
    return s1
S=input("Enter a string: ")
if (palindrome(S)==S):
    print(S, "is a palindrome")
else:
    print(S, "is not a palindrome")
print()
    
#3
def factorial(m):
    s=1
    for i in range(1,m+1):
        s*=i
    return s

def pascal(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
            
        print()
N=int(input("Enter a number: ")) 
pascal(N)
print()

#4
def panagram(str):
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for char in alphabet:
if char not in str.lower():return False

        return True
s=input()